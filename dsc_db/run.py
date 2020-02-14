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
from chemdataextractor.model.pv_model import PhotovoltaicCell, SentenceDye
from chemdataextractor.model import Compound

from dsc_db.model import PhotovoltaicRecord


def create_dsscdb_from_file(path):
    """
    Extract records from specific files tables.
    This contains the main algorithm.
    """

    # Load the document from the file
    with open(path, 'rb') as f:
        doc = Document.from_file(f)

    # Only add the photovoltaiccell and Compound models to the document
    doc.add_models([PhotovoltaicCell, Compound, SentenceDye])

    # Get all records from the table
    # This returns a tuple of type (pv_record, table)
    # The table object contains all the other records that were extracted
    table_records = get_table_records(doc)

    # Create PhotovoltaicRecord object
    pv_records = [PhotovoltaicRecord(record, table) for record, table in table_records]

    # When no Dye field is present, search contextually for it
    pv_records = add_dye_information(pv_records, doc)

    # Get the compound records for the next stage
    doc_records = [record.serialize() for record in doc.records]
    compound_records = [record['Compound'] for record in doc_records if 'Compound' in record.keys()]

    # Merge other information from inside the document when appropriate
    for record in pv_records:
        # Substituting in the definitions from the entire document
        if record.dye is not None:
            record._substitute_definitions('dye', 'Dye', doc)

        # Substituting the compound names for the dye
        if record.dye is not None:
            record._substitute_compound('dye', 'Dye', compound_records)

    # print the output
    for pv_record in pv_records:
        pp.pprint(pv_record.serialize())


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


def add_contextual_dye_from_document(pv_records, elements):
    """Merge contextually via a proximity based search for appropriate records"""

    # Group the records by table
    tables = {}
    for pv_record in pv_records:
        table = str(pv_record.table)
        if table not in tables.keys():
            tables[table] = [pv_record]
        else:
            tables[table].append(pv_record)

    latest_dye = None

    # Loop through elements, making note of surface dye instances
    for el in elements:

        # Add the latest dye information if detected...
        if isinstance(el, Table) and str(el) in tables.keys() and latest_dye is not None:
            print('Table detected: %s' % tables[str(el)])
            for record in tables[str(el)]:
                latest_dye['contextual'] = 'document'
                record.dye = {'Dye': [latest_dye]}

        # Update latest dye
        else:
            for record in el.records:
                serialized_record = record.serialize()
                if 'SentenceDye' in serialized_record.keys():
                    if 'raw_value' in serialized_record['SentenceDye'].keys():
                        latest_dye = serialized_record['SentenceDye']

    return pv_records


def add_dye_information(pv_records, doc):
    """
    Function to add dye information from document if possible, following this logic:
    1) Check the table caption, using DyeSentence
    2) Check rest of document via proximity

    All these sections could begin with a search for compounds, and then follow this by a search for common dyes like N719...
    :return: updated records
    """

    # Step 1: Check the caption using the DyeSentence parser
    # If found, this record is set with a 'contextual' flag to show that it was not taken directly from the table
    for pv_record in pv_records:
        if pv_record.dye is None:

            caption = pv_record.table.caption
            caption_records = [record.serialize() for record in caption.records]
            for cap_record in caption_records:

                if 'SentenceDye' in cap_record.keys() and pv_record.dye is None:
                    print('Dye record found! %s ' % cap_record['SentenceDye'])
                    cap_record['SentenceDye']['contextual'] = 'table'
                    pv_record.dye = {'Dye': [cap_record['SentenceDye']]}

                elif 'SentenceDye' in cap_record.keys():
                    cap_record['SentenceDye']['contextual'] = 'table'
                    pv_record.dye['Dye'].append(cap_record['SentenceDye'])

    # Step 2: Where no success in the caption, try merging with the closest proximity mention of a Dye in prose.
    pv_records = add_contextual_dye_from_document(pv_records, doc.elements)

    return pv_records


if __name__ == '__main__':
    create_dsscdb_from_file('/home/edward/pv/webscraping/rsc/articles/subset for development/C6RA14857C.html')

    # /home/edward/pv/webscraping/elsevier/articles/failed_training_downloads/S1385894717300542.xml')