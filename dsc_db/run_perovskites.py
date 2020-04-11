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
from dsc_db.data import all_dyes, blacklist_headings
from dsc_db.smiles import add_smiles

perovskite_properties = [
    ('SimulatedSolarLightIntensity', 'solar_simulator')
]

peroskite_material_properties = [
    ('Perovskite', 'perovskite'),
    ('HoleTransportLayer', 'htl')
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

    # When no Perovskite field is present, search contextually for it
    pv_records = add_perovskite_information(pv_records, filtered_elements)

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


def add_perovskite_information():
    pass

def add_distributor_info():
    # Will have to be done for HTM and perovskite
    pass

def add_smiles():
    pass