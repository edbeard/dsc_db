"""
Scripts for post-processing and merging results specific for a perovskite PV database.

Valid results must include a perovskite material and hole transporting later, and at least one photovoltaic property
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""


import logging
import pprint as pp

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

from chemdataextractor.doc import Document, Table
from chemdataextractor.model.pv_model import PerovskiteSolarCell, SentenceDye, CommonSentenceDye, SimulatedSolarLightIntensity, Substrate, Semiconductor, SentenceDyeLoading, SentenceSemiconductor
from chemdataextractor.model import Compound

from dsc_db.run import get_table_records, get_filtered_elements, add_contextual_info
from dsc_db.model import PhotovoltaicRecord, PerovskiteRecord
from dsc_db.data import  blacklist_headings, all_perovskites, all_htls, all_etls
from dsc_db.smiles import add_smiles

perovskite_properties = [
    ('SimulatedSolarLightIntensity', 'solar_simulator')
]

peroskite_material_properties = [
    ('Perovskite', 'perovskite'),
    ('HoleTransportLayer', 'htl'),
    ('ElectronTransportLayer', 'etl')
]


def create_pdb_from_file(path):
    """
    Extract records from specific files tables.
    This contains the main algorithm.
    """

    # Load the document from the file
    with open(path, 'rb') as f:
        doc = Document.from_file(f)

        # Only add the photovoltaiccell and Compound models to the document
    doc.add_models([PerovskiteSolarCell, Compound])  # Substrate, SentenceSemiconductor, DyeLoading])

    # Get all records from the table
    # This returns a tuple of type (pv_record, table)
    # The table object contains all the other records that were extracted
    table_records = get_table_records(doc, 'PerovskiteSolarCell')

    # Create PhotovoltaicRecord object
    pv_records = [PerovskiteRecord(record, table) for record, table in table_records]

    filtered_elements = get_filtered_elements(doc)

    # And contextual information from perovskites
    pv_records = add_contextual_info(pv_records, filtered_elements, peroskite_material_properties)

    # Get all compound records for the next stage
    doc_records = [record.serialize() for record in doc.records]
    compound_records = [record['Compound'] for record in doc_records if 'Compound' in record.keys()]

    # Filtering our results that don't contain voc, jsc, ff or PCE (if not running in debug mode)
    debug = False
    if not debug:
        pv_records = [pv_record for pv_record in [pv_records] if
                      any([getattr(pv_record, 'voc', 'None'), getattr(pv_record, 'jsc', 'None'),
                           getattr(pv_record, 'ff', 'None'), getattr(pv_record, 'pce', 'None')])]

    # Merge other information from inside the document when appropriate
    for record in pv_records:
        # Substituting in the definitions from the entire document
        if record.dye is not None:
            record._substitute_definitions('perovskite', 'Perovskite', doc)

        # Substituting the compound names for the perovskite
        if record.dye is not None:
            record._substitute_compound('perovskite', 'Perovskite', compound_records)

    # Contextual merging of perovskites complete, filtering out results without perovskites
    if not debug:
        pv_records = [pv_record for pv_record in pv_records if pv_record.perovskite is not None]

    # Apply sentence parsers for contextual information (Irradiance etc)
    pv_records = add_contextual_info(pv_records, filtered_elements, perovskite_properties)

    # Add chemical data from distributor of common dyes
    pv_records = add_distributor_info(pv_records)

    # Add SMILES through PubChem and ChemSpider where not added by distributor
    pv_records = add_smiles(pv_records)

    for pv_record in pv_records:
        pp.pprint(pv_record.serialize())

    # print the output after dyes removed...
    # for pv_record in pv_records:
    #     pp.pprint(pv_record.serialize())

    # Output sentence dye records for debugging
    # output_sentence_dyes(doc)

    return pv_records


def add_distributor_info(pv_records):
    """
    Adds useful information from dictionaries for common values of perovskites, HTLs and ETLs.
    :param pv_records: List of PhotovoltaicRecords object
    :return:pv_records: List of PhotovoltaicRecords object with dye information added
    """

    for pv_record in pv_records:
        # Add perovskite info
        if getattr(pv_record, 'perovskite', 'None'):
            for key, perovskite in all_perovskites.items():
                if pv_record.perovskite['Perovskite'].get('raw_value') in perovskite['labels'] and getattr(pv_record.perovskite['Perovskite'], 'raw_value', 'None'):
                    pv_record.perovskite['Perovskite']['formula'] = all_perovskites[key]['formula']
                    pv_record.perovskite['Perovskite']['name'] = all_perovskites[key]['name']
                    pv_record.perovskite['Perovskite']['labels'] = all_perovskites[key]['labels']

        # Add info on the hole transport layer
        if getattr(pv_record, 'htl', 'None'):
            for key, htl in all_htls.items():
                if pv_record.htl['HoleTransportLayer'].get('raw_value') in htl['labels'] and getattr(pv_record.htl['HoleTransportLayer'], 'raw_value', 'None'):
                    pv_record.htl['HoleTransportLayer']['smiles'] = all_htls[key]['smiles']
                    pv_record.htl['HoleTransportLayer']['name'] = all_htls[key]['name']
                    pv_record.htl['HoleTransportLayer']['labels'] = all_htls[key]['labels']

        # Add info on the electron transport layer
        if getattr(pv_record, 'etl', 'None'):
            for key, etl in all_etls.items():
                if pv_record.etl['ElectronTransportLayer'].get('raw_value') in etl['labels'] and getattr(pv_record.etl['ElectronTransportLayer'], 'raw_value', 'None'):
                    if 'structure' in all_etls[key].keys():
                       pv_record.etl['ElectronTransportLayer']['structure'] = all_etls[key]['structure']
                    pv_record.etl['ElectronTransportLayer']['name'] = all_etls[key]['name']
                    pv_record.etl['ElectronTransportLayer']['labels'] = all_etls[key]['labels']

    return pv_records


def add_smiles():
    # TODO: Add SMILES logic after determining which properties will require it.
    pass