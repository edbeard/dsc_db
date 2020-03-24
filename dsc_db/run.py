"""
Scripts for post-processing and merging results specific for a PV database.

Valid results must include a dye and at least one photovoltaic property
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import logging
import pprint as pp

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

from chemdataextractor.doc import Document, Table
from chemdataextractor.model.pv_model import PhotovoltaicCell, SentenceDye, CommonSentenceDye
from chemdataextractor.model import Compound

from dsc_db.model import PhotovoltaicRecord
from dsc_db.data import all_dyes, blacklist_headings
from dsc_db.smiles import add_smiles


def create_dsscdb_from_file(path):
    """
    Extract records from specific files tables.
    This contains the main algorithm.
    """

    # Load the document from the file
    with open(path, 'rb') as f:
        doc = Document.from_file(f)

    # Only add the photovoltaiccell and Compound models to the document
    doc.add_models([PhotovoltaicCell, Compound, SentenceDye, CommonSentenceDye])

    # Get all records from the table
    # This returns a tuple of type (pv_record, table)
    # The table object contains all the other records that were extracted
    table_records = get_table_records(doc)

    # Create PhotovoltaicRecord object
    pv_records = [PhotovoltaicRecord(record, table) for record, table in table_records]

    # When no Dye field is present, search contextually for it
    pv_records = add_dye_information(pv_records, doc)

    print(str(pv_records))

    print('Printing the PV records after adding dyes contextually:')
    for pv_record in pv_records:
        pp.pprint(pv_record.serialize())

    # Get the compound records for the next stage
    doc_records = [record.serialize() for record in doc.records]
    compound_records = [record['Compound'] for record in doc_records if 'Compound' in record.keys()]

    # Filtering our results that don't contain voc, jsc, ff and PCE (if not running in debug mode)
    debug = False
    if not debug:
        pv_records = [pv_record for pv_record in pv_records if getattr(pv_record, 'voc', 'None') and getattr(pv_record, 'jsc', 'None')
                      and getattr(pv_record, 'ff', 'None') and getattr(pv_record, 'pce', 'None')]

    # Merge other information from inside the document when appropriate
    for record in pv_records:
        # Substituting in the definitions from the entire document
        if record.dye is not None:
            record._substitute_definitions('dye', 'Dye', doc)

        # Substituting the compound names for the dye
        if record.dye is not None:
            record._substitute_compound('dye', 'Dye', compound_records)

    # print the output before dyes removed...
    for pv_record in pv_records:
        pp.pprint(pv_record.serialize())

    # Contextual merging of dyes complete, filtering out results without dyes
    pv_records = [pv_record for pv_record in pv_records if pv_record.dye is not None]

    # Add chemical data from distributor of common dyes
    pv_records = add_distributor_info(pv_records)

    # Add SMILES through PubChem and ChemSpider where not added by distributor
    pv_records = add_smiles(pv_records)

    # print the output after dyes removed...
    for pv_record in pv_records:
        pp.pprint(pv_record.serialize())

    # Output sentence dye records for debugging
    output_sentence_dyes(doc)

    return pv_records


def add_distributor_info(pv_records):
    """
    Adds useful information from dictionaries from various publishers
    :param pv_records: List of PhotovoltaicRecords object
    :return:pv_records: List of PhotovoltaicRecords object with dye information added
    """

    for key, dye in all_dyes.items():
        for pv_record in pv_records:
            for pv_dye in pv_record.dye['Dye']:
                if pv_dye.get('raw_value') in dye['labels'] and pv_dye.get('raw_value') is not None:
                    pv_dye['smiles'] = all_dyes[key]['smiles']
                    pv_dye['name'] = all_dyes[key]['name']
                    pv_dye['labels'] = all_dyes[key]['labels']

    return pv_records


def output_to_file(pv_records, output_path='/home/edward/pv/extractions/output'):
    """
    Outputs the pv_records to a file
    :param pv_records:
    :param output_path:
    :return:
    """

    serialized_records = [pp.pformat(record.serialize()) + '\n' for record in pv_records]

    with open(output_path, 'w') as outf:
        for record in serialized_records:
            outf.write(record + '\n')


def output_sentence_dyes(doc):
    """ Fucntion for outputting all detected sentence dyes. Used in debugging only"""

    # Print all the sentence Dyes
    print('The common sentence dye records:')
    for record in doc.records:
        record_dict = record.serialize()
        if 'CommonSentenceDye' in record_dict.keys():
            print(record_dict['CommonSentenceDye'])

    print('The sentence dye records:')
    for record in doc.records:
        record_dict = record.serialize()
        if 'SentenceDye' in record_dict.keys():
            print(record_dict['SentenceDye'])


def get_compound_records(doc):
    """ Function to extract the compound records from the entire document.
        Returns a list of compound records, enriched with names and roles from the document...
        :param chemdataextractor.Document doc : Document used to extract
        :return Tuple(pv_record, chemdataextractor.table) tables_record : All Photovoltaic records
    """

    doc.add_models(Compound)
    records = doc.records
    compounds = [record.serialize() for record in records]
    return compounds


def get_table_records(doc):
    """ Function to extract the photovoltaic device information from tables.
        Returns a tuple of (pv_record, table) for each PhotovoltaicCell records that is determined.
        Note that each Table has its id set to the enumerated index, for later merging.
        :param chemdataextractor.Document doc : Document used to extract
        :return Tuple(pv_record, chemdataextractor.table) tables_record : All Photovoltaic records

    """

    table_records = []
    # Obtain the PhotovoltaicCell records from each table
    for table in doc.tables:
        records = [record.serialize()['PhotovoltaicCell'] for record in table.records if 'PhotovoltaicCell' == record.__class__.__name__]
        for record in records:
            table_records.append((record, table))

    return table_records


def add_contextual_dye_from_document(pv_records, elements, permissive=True):
    """Merge contextually via a proximity based search for appropriate records"""

    if permissive:
        dye_key = 'SentenceDye'
        context = 'document_permissive'
    else:
        dye_key = 'CommonSentenceDye'
        context = 'document'

    # Group the records by table
    tables = {}
    for pv_record in pv_records:
        table = str(pv_record.table)
        if table not in tables.keys():
            tables[table] = [pv_record]
        else:
            tables[table].append(pv_record)

    latest_dye = None

    # Loop through elements, making note of sentence dye instances
    for el in elements:

        # Add the latest dye information if detected...
        if isinstance(el, Table) and str(el) in tables.keys() and latest_dye is not None:
            print('Table detected: %s' % tables[str(el)])
            for record in tables[str(el)]:
                if record.dye is None:
                    latest_dye['contextual'] = context
                    record.dye = {'Dye': [latest_dye]}

        # Update latest dye
        else:
            for record in el.records:
                if record.__class__.__name__ == dye_key:
                    serialized_record = record.serialize()
                    if 'raw_value' in serialized_record[dye_key].keys():
                        latest_dye = serialized_record[dye_key]

    return pv_records


def add_contextual_dye_from_document_by_multiplicity(pv_records, filtered_elements, permissive=False):
    """
    Merge dye information contextually under assumption that the most common dye mentioned in the methods section
    :param pv_records:
    :return:
    """

    # Use different parsin results for permissive and non-permissive approaches
    if permissive:
        dye_key = 'SentenceDye'
        context = 'document_permissive'
    else:
        dye_key = 'CommonSentenceDye'
        context = 'document'

    # Count occurrence in the filtered element list
    altered = False # Boolean indicating whether the following logic altered the photovoltaic records
    sentence_dyes = []
    sentence_dye_records = [record.serialize() for el in filtered_elements for record in el.records if record.__class__.__name__ == dye_key]
    if not sentence_dye_records:
        return pv_records, altered
    for record in sentence_dye_records:
        if 'raw_value' in record[dye_key].keys():
            sentence_dyes.append(record[dye_key]['raw_value'])

    # If a dye was found, output
    if sentence_dyes:
        altered = True

    most_common_dyes = get_most_common_dyes(sentence_dyes)

    # Substitute in the most common dye, if found
    if len(most_common_dyes) == 1:
        for pv_record in pv_records:
            if pv_record.dye is None:
                dye = {'contextual': context, 'raw_value': most_common_dyes[0]}
                pv_record.dye = {'Dye': [dye]}

    return pv_records, altered


def add_contextual_dye_from_table_caption_by_multiplicity(pv_records, permissive=False):
    """Add contextual Dye information from the caption if possible """

    # Use different parsing results for permissive and non-permissive approaches
    if permissive:
        dye_key = 'SentenceDye'
        context = 'table_caption_permissive'
    else:
        dye_key = 'CommonSentenceDye'
        context = 'table_caption'

    altered = False
    for pv_record in pv_records:
        if pv_record.dye is None:
            caption = pv_record.table.caption
            common_dye_caption_records = [record.serialize() for record in caption.records if record.__class__.__name__ == dye_key]
            caption_dyes = []
            for cap_record in common_dye_caption_records:

                if cap_record[dye_key].get('raw_value'):
                    caption_dyes.append(cap_record[dye_key]['raw_value'])

    # If a dye was found, output
    if caption_dyes:
        altered = True

    most_common_dyes = get_most_common_dyes(caption_dyes)

    # Substitute in the most common dye, if found
    if len(most_common_dyes) == 1:
        for pv_record in pv_records:
            if pv_record.dye is None:
                dye = {'contextual': context, 'raw_value': most_common_dyes[0]}
                pv_record.dye = {'Dye': [dye]}

    return pv_records, altered


def get_most_common_dyes(sentence_dyes):
    """ Takes a list of extracted dye names, and creates a list of the most common.
     If list has a length greater than 1, there was an equal occurance of 2+ dyes.
     Such cases are not added for higher precision."""

    dye_names = list(set(sentence_dyes))
    dye_count = []
    for dye in dye_names:
        dye_count.append(sentence_dyes.count(dye))

    if dye_count:
        max_value = max(dye_count)
    most_common_dyes = [dye for i, dye in enumerate(dye_names) if dye_count[i] == max_value]

    return most_common_dyes


def add_dye_information(pv_records, doc):
    """
    Function to add dye information from document if possible, following this logic:
    1) Check the table caption, using DyeSentence
    2) Check rest of document for commonly distributed dyes, by proximity
    3) Check rest of document with more permissive logic (alphanumic regex), by proximity

    All these sections could begin with a search for compounds, and then follow this by a search for common dyes like N719...
    :return: updated records
    """

        # print('Dye record found! %s ' % cap_record['CommonSentenceDye'])
                    # cap_record['CommonSentenceDye']['contextual'] = 'table'
                    # pv_record.dye = {'Dye': [cap_record['CommonSentenceDye']]}

    # Step 1b: Check the table caption using the more-permissive DyeSentence parser
    # If found, this record is set with a contextual flag to show it was not taken from the table...

            #
            #
            #
            #
            # permissive_dye_caption_records = [record.serialize() for record in caption.records if
            #                                   record.__class__.__name__ == 'CommonSentenceDye']
            #
            #     if 'SentenceDye' in cap_record.keys() and pv_record.dye is None:
            #         print('Dye record found! %s ' % cap_record['SentenceDye'])
            #         cap_record['SentenceDye']['contextual'] = 'table_permissive'
            #         pv_record.dye = {'Dye': [cap_record['SentenceDye']]}
            #
            #     elif 'SentenceDye' in cap_record.keys():
            #         cap_record['SentenceDye']['contextual'] = 'table'
            #         pv_record.dye['Dye'].append(cap_record['SentenceDye'])


    # Step 1: Merge with available common industrial dyes by frequency of occurrence
    # pv_records, altered = add_contextual_dye_from_document_by_multiplicity(pv_records, permissive=False)

    # TODO: Delete the above when the logic below is working correctly

    altered = False

    # Step 1: Check the caption using the CommonDyeSentence parser
    # If found, this record is set with a 'contextual' flag to show that it was not taken directly from the table
    pv_records, altered = add_contextual_dye_from_table_caption_by_multiplicity(pv_records, permissive=False)
    if altered:
        return pv_records

    # Step 1b: Check the caption using the more permissive DyeSentence parser
    pv_records, altered = add_contextual_dye_from_table_caption_by_multiplicity(pv_records, permissive=True)
    if altered:
        return pv_records

    # When no Dye found from the caption, attempt to find from the body of text for specific sections

    # Filter through the document elements to only obtain those that are allowed in the merging algorithm
    # (ie. removing any sections mentioning introduction or results)
    filtered_elements = []
    allow_heading = True
    elements = doc.elements
    for el in elements:
        if el.__class__.__name__ == 'Heading':
            allow_heading = True
            # Check if any token matches the blacklist
            for token_list in el.raw_tokens:
                for token in token_list:
                    if token.lower() in blacklist_headings:
                        allow_heading = False
                        break

        if allow_heading:
            filtered_elements.append(el)

    # Step 2: Merge with available common industrial dyes by frequency of occurrence
    pv_records, altered = add_contextual_dye_from_document_by_multiplicity(pv_records, filtered_elements, permissive=False)
    if altered:
        return pv_records

    # Step 3: If no common industrial dye found, repeat with more lenient dye matching
    pv_records, _ = add_contextual_dye_from_document_by_multiplicity(pv_records, filtered_elements, permissive=True)

    return pv_records


if __name__ == '__main__':
    import cProfile, pstats, io
    path = "/home/edward/pv/extractions/input/10.1016:j.jelechem.2017.12.050.xml"
    cProfile.runctx("create_dsscdb_from_file(path)", None, locals=locals())

    # Create stream for progiler to write to
    profiling_output = io.StringIO()
    p = pstats.Stats('mainstats', stream=profiling_output)

    # Print resilts to that stream
    # This puts the top 30 functions, sorted by time spent in each
    p.strip_dirs().sort_stats('cumulative').print_stats(30)

    #Print the results to log
    print('Profiling results: %s' % profiling_output.getvalue())
    profiling_output.close()
    print('Output ends')





    # /home/edward/pv/webscraping/elsevier/articles/failed_training_downloads/S1385894717300542.xml')