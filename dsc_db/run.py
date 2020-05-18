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
from chemdataextractor.model.pv_model import PhotovoltaicCell, SentenceDye, CommonSentenceDye, SimulatedSolarLightIntensity, Substrate, Semiconductor, SentenceDyeLoading, SentenceSemiconductor
from chemdataextractor.model import Compound, ListType, FloatType
from chemdataextractor.model.units.unit import UnitType

from dsc_db.model import PhotovoltaicRecord
from dsc_db.data import all_dyes, blacklist_headings, redox_couples
from dsc_db.smiles import add_smiles
from dsc_db.calculate import calculate_metrics, calculate_relative_metrics, round_to_sig_figs
import sigfig

# Properties to be merged from contextual sentences
dsc_properties = [('RedoxCouple', 'redox_couple'),
    ('SimulatedSolarLightIntensity', 'solar_simulator'),
              ('Semiconductor', 'semiconductor'),
              ('SentenceDyeLoading', 'dye_loading'),
              ('Substrate', 'substrate'),
                ('ActiveArea', 'active_area')]

calc_properties_to_add = {
    'solar_simulator': 'SimulatedSolarLightIntensity',
    'jsc': 'ShortCircuitCurrentDensity',
    'isc': 'ShortCircuitCurrent'
}


def create_dsscdb_from_file(doc):
    """
    Extract records from specific files tables.
    This contains the main algorithm.
    :param doc = CDE Document object
    """

    # Only add the photovoltaiccell and Compound models to the document
    doc.add_models([PhotovoltaicCell, Compound, SentenceDye, CommonSentenceDye, SimulatedSolarLightIntensity, SentenceSemiconductor, SentenceDyeLoading])# Substrate, SentenceSemiconductor, DyeLoading])

    filtered_elements = get_filtered_elements(doc)

    # Get the active_area property if available, used in calculating properties
    active_area_record  = get_active_area(filtered_elements)

    # Get all records from the table
    # This returns a tuple of type (pv_record, table)
    # The table object contains all the other records that were extracted
    table_records = get_table_records(doc, 'PhotovoltaicCell', active_area_record)

    # Create PhotovoltaicRecord object
    pv_records = [PhotovoltaicRecord(record, table) for record, table in table_records]

    # print('Printing the results after table extraction only')
    # for pv_record in pv_records:
    #     pp.pprint(pv_record.serialize())

    # When no Dye field is present, search contextually for it
    pv_records = add_dye_information(pv_records, filtered_elements)

    # print(str(pv_records))

    # print('Printing the PV records after adding dyes contextually:')
    # for pv_record in pv_records:
    #     pp.pprint(pv_record.serialize())

    # Get the compound records for the next stage
    doc_records = [record.serialize() for record in doc.records]
    compound_records = [record['Compound'] for record in doc_records if 'Compound' in record.keys()]

    # Filtering our results that don't contain the variables voc, jsc, ff and PCE (if not running in debug mode)
    debug = False
    if not debug:
        pv_records = [pv_record for pv_record in pv_records if any([getattr(pv_record, 'voc', False), getattr(pv_record, 'jsc', False),
                                                 getattr(pv_record, 'ff', False), getattr(pv_record, 'pce', False)])]

    # Merge other information from inside the document when appropriate
    for record in pv_records:
        # Substituting in the definitions from the entire document
        if record.dye is not None:
            record._substitute_definitions('dye', 'Dye', doc)

        # Substituting the compound names for the dye
        if record.dye is not None:
            record._substitute_compound('dye', 'Dye', compound_records)

    # print the output before dyes removed...
    # print('Printing output after the contextual Dye information is added...')
    # for pv_record in pv_records:
    #     pp.pprint(pv_record.serialize())

    # Contextual merging of dyes complete, filtering out results without dyes
    if not debug:
        # Remove results without a dye
        pv_records = [pv_record for pv_record in pv_records if pv_record.dye is not None]

    # Apply sentence parsers for contextual information (Irradiance etc)
    pv_records = add_contextual_info(pv_records, filtered_elements, dsc_properties)
    # print('Printing output after contextual info is added from the caption and document body...')
    # for pv_record in pv_records:
    #     pp.pprint(pv_record.serialize())


    # Add chemical data from distributor of common dyes
    pv_records = add_distributor_info(pv_records)

    # Add SMILES through PubChem and ChemSpider where not added by distributor
    pv_records = add_smiles(pv_records)
    # print('Printing output after smiles are added ...')
    # for pv_record in pv_records:
    #     pp.pprint(pv_record.serialize())

    # Merge calculated properties
    pv_records = add_calculated_properties(pv_records)
    # print('Printing output after extra properties are calculated...')
    # for pv_record in pv_records:
    #     pp.pprint(pv_record.serialize())

    # print the output after dyes removed...
    # for pv_record in pv_records:
    #     pp.pprint(pv_record.serialize())

    # Output sentence dye records for debugging
    # output_sentence_dyes(doc)

    return pv_records


def get_active_area(filtered_elements):
    """
    Obtains the active area (if available) from filtered document elements
    """

    filtered_record = [get_standardized_values_single_property(record).serialize() for el in filtered_elements for record in el.records if
                                          record.__class__.__name__ == 'ActiveArea']

    active_area_records = [record for record in filtered_record if record['ActiveArea'].get('raw_value')]

    sentence_values = [rec['ActiveArea']['value'] for rec in active_area_records]

    if sentence_values:
        all_equal = sentence_values.count(sentence_values[0]) == len(sentence_values)
        if all_equal:
            active_area_records[0]['ActiveArea']['contextual'] = 'document'
            return active_area_records[0]


def add_calculated_properties(pv_records):
    """
    Uses the calculated_properties field to add data
    """
    for pv_record in pv_records:
        if pv_record.calculated_properties is not None:
            if 'solar_simulator' in pv_record.calculated_properties.keys():
                if pv_record.solar_simulator is not None:
                    pv_record.solar_simulator['SimulatedSolarLightIntensity']['calculated_value'] = pv_record.calculated_properties['solar_simulator']['value']
                else:
                    pv_record.solar_simulator = {'SimulatedSolarLightIntensity': {'calculated_value': pv_record.calculated_properties['solar_simulator']['value']}}

                pv_record.solar_simulator['SimulatedSolarLightIntensity']['calculated_units'] = pv_record.calculated_properties['solar_simulator']['units']
                pv_record.solar_simulator['SimulatedSolarLightIntensity']['calculated_error'] = pv_record.calculated_properties['solar_simulator']['error']

            if 'isc' in pv_record.calculated_properties.keys():
                if pv_record.isc is not None:
                    pv_record.isc['ShortCircuitCurrent']['calculated_value'] = pv_record.calculated_properties['isc']['value']
                else:
                    pv_record.isc = {'ShortCircuitCurrent': {'calculated_value': pv_record.calculated_properties['isc']['value']}}

                pv_record.isc['ShortCircuitCurrent']['calculated_units'] = pv_record.calculated_properties['isc']['units']
                pv_record.isc['ShortCircuitCurrent']['calculated_error'] = pv_record.calculated_properties['isc']['error']

            if 'jsc' in pv_record.calculated_properties.keys():
                if pv_record.jsc is not None:
                    pv_record.jsc['ShortCircuitCurrentDensity']['calculated_value'] = pv_record.calculated_properties['jsc']['value']
                else:
                    pv_record.jsc = {'ShortCircuitCurrentDensity': {'calculated_value': pv_record.calculated_properties['jsc']['value']}}

                pv_record.jsc['ShortCircuitCurrentDensity']['calculated_units'] = pv_record.calculated_properties['jsc']['units']
                pv_record.jsc['ShortCircuitCurrentDensity']['calculated_error'] = pv_record.calculated_properties['jsc']['error']

        else:
            pp.pprint(pv_record.serialize())

    return pv_records


def get_filtered_elements(doc):

    # Filter through the document elements to obtain the 'methods' section
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

    return filtered_elements


def add_contextual_info(pv_records, filtered_elements, properties):
    """ Add contextual information on dye extraction from the document using the specified sentence parsers
    :param pv_records: List of PV record objects
    :param properties: List of tuples containing the field and model names to be merged contextually.
    :param filtered_elements: List of elements from the document that describe the experimental method.
    """

    # Create a list containing document records for each property:
    sentence_records = []
    for parser, field in properties:
        filtered_record = [get_standardized_values_single_property(record).serialize() for el in filtered_elements for record in el.records if
                                              record.__class__.__name__ == parser]

        element_records = [record for record in filtered_record if record[parser].get('raw_value')]
        # Merge equivalent names together
        element_records = merge_redox_couples(element_records)
        sentence_records.append(element_records)

    for pv_record in pv_records:
        caption = pv_record.table.caption
        for i, props in enumerate(properties):
            parser, field = props[0], props[1]
            if getattr(pv_record, field) is None:
                # First, search the caption for this
                caption_records = [get_standardized_values_single_property(record).serialize() for record in caption.records if
                                              record.__class__.__name__ == parser]
                caption_records = [record for record in caption_records if record[parser].get('raw_value')]
                caption_records = merge_redox_couples(caption_records)

                # Then, count the occurrences. If there is only one result, merge (as we can assume this applies to all the
                # results in the table.
                try:
                    caption_values = [rec[parser]['value'] for rec in caption_records]
                except:
                    caption_values = [rec[parser]['raw_value'] for rec in caption_records]

                if caption_values:
                    all_equal = caption_values.count(caption_values[0]) == len(caption_values)
                    if all_equal:
                        caption_records[0][parser]['contextual'] = 'table_caption'
                        setattr(pv_record, field, caption_records[0])
                else:
                    # Otherwise, extract from the filtered elements
                    records_for_this_field = sentence_records[i]
                    try:
                        sentence_values = [rec[parser]['value'] for rec in records_for_this_field]
                    except:
                        sentence_values = [rec[parser]['raw_value'] for rec in records_for_this_field]
                        # print(sentence_records[0][parser])
                    if sentence_values:
                        all_equal = sentence_values.count(sentence_values[0]) == len(sentence_values)
                        if all_equal:
                            records_for_this_field[0][parser]['contextual'] = 'document'
                            setattr(pv_record, field, records_for_this_field[0])

    return pv_records


def add_distributor_info(pv_records):
    """
    Adds useful information from dictionaries from various publishers
    :param pv_records: List of PhotovoltaicRecords object
    :return:pv_records: List of PhotovoltaicRecords object with dye information added
    """

    for key, dye in all_dyes.items():
        for pv_record in pv_records:
            if pv_record.dye:
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


def get_table_records(doc, record_type, active_area_record=None, model_field_dict=calc_properties_to_add):
    """ Function to extract the photovoltaic device information from tables.
        Returns a tuple of (pv_record, table) for each PhotovoltaicCell records that is determined.
        Note that each Table has its id set to the enumerated index, for later merging.
        :param chemdataextractor.Document doc : Document used to extract
        :param record_type : the name of the model of record to target
        :param active_area_record: The contextual records containing active area data (if applicable)
        :param model_field_dict: Dict of field-model pairs for properties being calculated.

        :return Tuple(pv_record, chemdataextractor.table) tables_record : All Photovoltaic records

    """

    table_records = []
    # Obtain the PhotovoltaicCell records from each table
    for table in doc.tables:
        records = []
        for record in table.records:
            if record_type == record.__class__.__name__:
                # Remove sub_records that only contain a specifier
                record = remove_specifiers_only(record)

                # Create dictionary of record data
                record = get_standardized_values(record)
                serialized_record = record.serialize()[record_type]

                # Add calculated properties to the pv_records
                record = calculate_metrics(record, active_area_record)
                if record.calculated_properties:
                    serialized_record['calculated_properties'] = {}
                for key, data in record.calculated_properties.items():
                    serialized_data = data.serialize()
                    calc_props = {'value': serialized_data[model_field_dict[key]]['value'],
                                  'units': serialized_data[model_field_dict[key]]['units'],
                                  'error': serialized_data[model_field_dict[key]]['error']}
                    serialized_record['calculated_properties'][key] = calc_props

                serialized_record['table_row_categories'] = record.table_row_categories

                records.append(serialized_record)

        # Add calculation of standardised properties
        records = calculate_relative_metrics(records)

        for record in records:
            table_records.append((record, table))

    return table_records


def remove_specifiers_only(record):
    """
    Automatically remove any records that only contain a specifier.
    As the specifier is always required, this is done by testing the length of the sub_records 'field' object
    :param record : cde record object
    """

    for field in record.fields:
        sub_record = getattr(record, field)
        if sub_record:
            # Get the values that were populated
            populated_fields = [getattr(sub_record, sub_field) for sub_field in sub_record.fields if hasattr(sub_record, sub_field)]
            no_pop_fields = sum(field is not None for field in populated_fields)
            if no_pop_fields == 1:
                setattr(record, field, None)

    return record


def get_standardized_values(record):
    """
    Automatically get the standardized values for a record containing fields of other record objects.
    :param record : cde record object
    """

    for field in record.fields:
        sub_record = getattr(record, field)
        if sub_record:
            if getattr(sub_record, 'value', None) is not None and getattr(sub_record, 'units', None) is not None:
                # Standardize and add the units information
                sub_record.std_units = sub_record.units.dimensions.standard_units

                # Standardize the value information
                std_value = [sub_record.units.convert_value_to_standard(val) for val in sub_record.value]
                if getattr(sub_record, 'exponent', None) is not None and getattr(sub_record, 'exponent', None) != []:
                    std_value = [value * pow(10, int(sub_record.exponent[0])) for value in std_value]
                sub_record.std_value = std_value

                # Standardize the error information if present
                if getattr(sub_record, 'error', None) is not None:
                    std_error = sub_record.units.convert_error_to_standard(sub_record.error)
                    if getattr(sub_record, 'exponent', None) is not None and getattr(sub_record, 'exponent', None) != []:
                        # Assumes that the error is also expressed as part of this exponent
                        std_error = std_error * pow(10, int(sub_record.exponent[0]))
                    sub_record.std_error = std_error

    return record


def get_standardized_values_single_property(record):
    """
    Automatically get the standardized values for a single record where possible
    """
    if getattr(record, 'value', None) is not None and getattr(record, 'units', None) is not None:
        # Standardize and add the units information
        record.std_units = record.units.dimensions.standard_units

        # Standardize the value information
        std_value = [record.units.convert_value_to_standard(val) for val in record.value]
        if getattr(record, 'exponent', None) is not None and getattr(record, 'exponent', None) != []:
            std_value = [value * pow(10, int(record.exponent[0])) for value in std_value]
        record.std_value = std_value

        # Standardize the error information if present
        if getattr(record, 'error', None) is not None:
            std_error = record.units.convert_error_to_standard(record.error)
            if getattr(record, 'exponent', None) is not None and getattr(record, 'exponent', None) != []:
                std_error = std_error * pow(10, int(record.exponent[0]))
            record.std_error = std_error

    return record


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
            if len(most_common_dyes) == 1:
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


def add_dye_information(pv_records, filtered_elements):
    """
    Function to add contextual dye information from document where possible, by doing the following
    1) Search for common dyes in the table caption
    2) Search the methods section of the document for common dyes.
    3) Search with permissive dye search inside table caption.
    For each stage, if multiple results are returned the most common is assumed to be correct.

    :return: updated records
    """
    altered = False

    # Step 1: Check the table caption using the CommonDyeSentence parser
    pv_records, altered = add_contextual_dye_from_table_caption_by_multiplicity(pv_records, permissive=False)
    if altered:
        return pv_records

    # Step 2: Check the Methods section using the CommonDyeSentence parser
    pv_records, altered = add_contextual_dye_from_document_by_multiplicity(pv_records, filtered_elements, permissive=False)
    if altered:
        return pv_records

    # Step 3: Check the table caption using the more permissive DyeSentence parser
    pv_records, _ = add_contextual_dye_from_table_caption_by_multiplicity(pv_records, permissive=True)

    return pv_records


def merge_redox_couples(records):

    """
    Standardizing redox couple data based on the extracted string
    """

    for record in records:
        if 'RedoxCouple' in record.keys():
            raw_value = record['RedoxCouple']['raw_value']

            # Remove generic hyphen characters for matching
            characters_to_remove = '−−-'
            match_string = raw_value
            for char in characters_to_remove:
                match_string = match_string.replace(char, '')

            for key, item in redox_couples.items():
                if match_string in item['match']:
                    record['RedoxCouple']['value'] = key
                    record['RedoxCouple']['names'] = item['names']


    return records


if __name__ == '__main__':
    import cProfile, pstats, io
    path = "/home/edward/pv/extractions/input_filtered_tables/dsc/C1EE01196K.html"
    with open(path, 'rb') as f:
        doc = Document.from_file(f)
    cProfile.runctx("create_dsscdb_from_file(doc)", None, locals=locals())


    # Create stream for progiler to write to
    profiling_output = io.StringIO()
    p = pstats.Stats('mainstats', stream=profiling_output)






    # /home/edward/pv/webscraping/elsevier/articles/failed_training_downloads/S1385894717300542.xml')