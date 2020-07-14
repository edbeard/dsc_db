"""
Scripts for post-processing and merging results specific for a perovskite PV database.

Valid results must include a perovskite material and hole transporting later, and at least one photovoltaic property
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""


import logging
import pprint as pp

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

from chemdataextractor.doc import Document
from chemdataextractor.model.pv_model import PerovskiteSolarCell, SentencePerovskite
from chemdataextractor.model import Compound

from dsc_db.run import get_table_records, get_filtered_elements, add_contextual_info, get_active_area, add_derived_properties
from dsc_db.model import PerovskiteRecord
from dsc_db.data import  all_htls, all_etls, perovskite_abbreviations
from dsc_db.smiles import add_smiles_perovskite_htl

perovskite_properties = [
    ('SimulatedSolarLightIntensity', 'solar_simulator'),
    ('Substrate', 'substrate'),
    ('ActiveArea', 'active_area'),
    ('CounterElectrode', 'counter_electrode')
]

peroskite_material_properties = [
    ('SentencePerovskite', 'perovskite'),
    ('HoleTransportLayer', 'htl'),
    ('ElectronTransportLayer', 'etl')
]

structural_material_props_minus_perovskite = [
    ('Substrate', 'substrate'),
    ('CounterElectrode', 'counter_electrode'),
    ('HoleTransportLayer', 'htl'),
    ('ElectronTransportLayer', 'etl')
]


def create_pdb_from_file(doc):
    """
    Extract records from specific files tables.
    This contains the main algorithm.
    """

    # Only add the photovoltaiccell and Compound models to the document
    doc.add_models([PerovskiteSolarCell, Compound, SentencePerovskite])  # Substrate, SentenceSemiconductor, DyeLoading])

    filtered_elements = get_filtered_elements(doc) # Get the relevant filtered elements for merging

    # Get the active_area property if available, used in calculating properties
    active_area_record = get_active_area(filtered_elements)

    # Get all records from the table
    # This returns a tuple of type (pv_record, table)
    # The table object contains all the other records that were extracted
    table_records = get_table_records(doc, 'PerovskiteSolarCell', active_area_record)

    # Create PhotovoltaicRecord object
    pv_records = [PerovskiteRecord(record, table) for record, table in table_records]

    print('After initial table extraction:')
    for pv_record in pv_records:
        pp.pprint(pv_record.serialize())

    # And contextual information from perovskites
    pv_records = add_contextual_info(pv_records, filtered_elements, peroskite_material_properties)

    print('After adding contextual information from perovskites:')
    for pv_record in pv_records:
        pp.pprint(pv_record.serialize())

    # Get all compound records for the next stage
    doc_records = [record.serialize() for record in doc.records]
    compound_records = [record['Compound'] for record in doc_records if 'Compound' in record.keys()]

    # Filtering our results that don't contain voc, jsc, ff or PCE (if not running in debug mode)
    debug = False
    if not debug:
        pv_records = [pv_record for pv_record in pv_records if (
            all([getattr(pv_record, 'voc', False), getattr(pv_record, 'jsc', False)]) or
            all([getattr(pv_record, 'voc', False), getattr(pv_record, 'ff', False)]) or
            all([getattr(pv_record, 'voc', False), getattr(pv_record, 'pce', False)]) or
            all([getattr(pv_record, 'jsc', False), getattr(pv_record, 'ff', False)]) or
            all([getattr(pv_record, 'jsc', False), getattr(pv_record, 'pce', False)]) or
            all([getattr(pv_record, 'ff', False), getattr(pv_record, 'pce', False)])) ]

    print('After filtering out results without the 4 main properties:')
    for pv_record in pv_records:
        pp.pprint(pv_record.serialize())

    # Merge other information from inside the document when appropriate
    for record in pv_records:
        # Substituting in the definitions from the entire document for HTL
        if record.htl is not None:
            record._substitute_definitions('htl', 'HoleTransportLayer', doc)

        # Substituting the compound names for the perovskite
        if record.htl is not None:
            record._substitute_compound('htl', 'HoleTransportLayer', compound_records)

    # Contextual merging of perovskites complete, filtering out results without perovskites
    if not debug:
        pv_records = [pv_record for pv_record in pv_records if pv_record.perovskite is not None]

    # Apply sentence parsers for contextual information (Irradiance etc)
    pv_records = add_contextual_info(pv_records, filtered_elements, perovskite_properties)

    # Add chemical data from distributor of common perovskite materials, and from review papers
    pv_records = enhance_common_values(pv_records)

    # Add SMILES through PubChem and ChemSpider where not added by distributor
    pv_records = add_smiles_perovskite_htl(pv_records)

    for pv_record in pv_records:
        pp.pprint(pv_record.serialize())

    # Merge derived properties
    pv_records = add_derived_properties(pv_records)

    # Remove merged material properties that are likely to be incorrect
    pv_records = filter_contextual_properties_from_reviews(pv_records)

    # print the output after dyes removed...
    # for pv_record in pv_records:
    #     pp.pprint(pv_record.serialize())

    # Output sentence dye records for debugging
    # output_sentence_dyes(doc)

    return pv_records


def add_smiles(pv_records):
    # TODO: Add SMILES logic after determining which properties will require it.
    pass


def filter_contextual_properties_from_reviews(pv_records):
    """
    Filter out contextual material properties for results that contain a 'reference' property.
    Such records are assumed to be from review papers, where such information is liable to be specific to particular cases.

    These records are still deemed to be useful as all required info can be found in the corresponding record.
    """
    for pv_record in pv_records:
        if getattr(pv_record, 'ref') is not None:
            if 'value' in pv_record.ref['Reference'].keys():

                # Filter out all document contextual properties that are not the perovskite material
                for parser, field in structural_material_props_minus_perovskite:
                    if getattr(pv_record, field) is not None:
                        pv_field = getattr(pv_record, field)
                        if 'contextual' in pv_field[parser].keys():
                            if pv_field[parser]['contextual'] == 'document':
                                setattr(pv_record, field, None)

    return pv_records


def enhance_common_values(pv_records):
    """
    The Perovskite equivalent of add_distributor_info.
    Function adds extra useful information about perovskite properties (the perovskite material, the ETM and HTM) when
    possible.
    """

    # First add the ETL information

    for key, etl in all_etls.items():
        for pv_record in pv_records:
            if pv_record.etl:
                if pv_record.etl['ElectronTransportLayer'].get('raw_value') is not None:
                    if pv_record.etl['ElectronTransportLayer'].get('raw_value').replace(' / ', '/').replace(' - ', '-') in etl['labels'] or \
                        pv_record.etl['ElectronTransportLayer'].get('raw_value').lower() in etl['labels']:
                        pv_record.etl['ElectronTransportLayer']['name'] = all_etls[key]['name']
                        pv_record.etl['ElectronTransportLayer']['labels'] = all_etls[key]['labels']
                        if 'structure' in all_etls[key].keys():
                            pv_record.etl['ElectronTransportLayer']['structure'] = all_etls[key]['structure']

    # Then add the HTl information...
    for key, htl in all_htls.items():
        for pv_record in pv_records:
            if pv_record.htl:
                if pv_record.htl['HoleTransportLayer'].get('raw_value') is not None:
                    if pv_record.htl['HoleTransportLayer'].get('raw_value').replace(' / ', '/').replace(' - ', '-') in htl['labels']:
                        pv_record.htl['HoleTransportLayer']['name'] = all_htls[key]['name']
                        pv_record.htl['HoleTransportLayer']['labels'] = all_htls[key]['labels']
                        pv_record.htl['HoleTransportLayer']['smiles'] = {'value': all_htls[key]['smiles'], 'context':'dict'}

    # Then, add the Perovskite information...
    # Step 2, Do a substitution for the common terms...
    for pv_record in pv_records:
        if pv_record.perovskite:
            if 'Perovskite' in pv_record.perovskite.keys():
                if pv_record.perovskite['Perovskite'].get('raw_value') is not None:
                    formula = pv_record.perovskite['Perovskite']['raw_value']
                    for key, val in perovskite_abbreviations.items():
                        formula = formula.replace(key, '(' + val + ')')
                    pv_record.perovskite['Perovskite']['formula'] = formula

            elif 'SentencePerovskite' in pv_record.perovskite.keys():
                formula = pv_record.perovskite['SentencePerovskite']['raw_value']
                for key, val in perovskite_abbreviations.items():
                    formula = formula.replace(key, '(' + val + ')')
                pv_record.perovskite['SentencePerovskite']['formula'] = formula

    return pv_records


if __name__ == '__main__':

    import cProfile, pstats, io
    path = "/home/edward/pv/extractions/input_filtered/psc/C6NR01010E.html"
    with open(path, 'rb') as f:
        doc = Document.from_file(f)
    cProfile.runctx("create_pdb_from_file(doc)", None, locals=locals())


    # Create stream for progiler to write to
    profiling_output = io.StringIO()
    p = pstats.Stats('mainstats', stream=profiling_output)
