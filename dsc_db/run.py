"""
Scripts for post-processing and merging results specific for a PV database.

Valid results must include a dye and at least one photovoltaic property
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import logging
import os
import pprint as pp

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

from chemdataextractor import Document
from chemdataextractor.model.pv_model import PhotovoltaicCell, SentenceDye
from chemdataextractor.model import Compound

from dsc_db.model import PhotovoltaicRecord


def create_dsscdb_from_file(path):
    """
    Extract records from specific files tables.
    This contains the main algorithm.
    """

    # Load the doucment from the file
    with open(path, 'rb') as f:
        doc = Document.from_file(f)

    # Only add the photovoltaiccell and Compound models to the document
    doc.add_models([PhotovoltaicCell, Compound])


    # Get all records from the table
    # This returns a tuple of type (pv_record, table)
    # The table object contains all the other records that were extracted
    table_records = get_table_records(doc)

    # Create PhotovoltaicRecord object
    pv_records = [PhotovoltaicRecord(record, doc, table) for record, table in table_records]

    # When no Dye field is present, search contextually for it
    pv_records = add_dye_information(pv_records)

    # Merge other information from inside the document when appropriate
    for record in pv_records:
        # Substituting in the definitions from the entire document
        if record.dye is not None:
            record._substitute_definitions('dye', 'Dye')

        # Substituting the compound names for the dye
        if record.dye is not None:
            record._substitute_compound('dye', 'Dye')

    # print the output
    for pv_record in pv_records:
        pp.pprint(pv_record.serialize())



    # Substituting in the compound information for counter electrode
    # for record in pv_records:
    #     print(record.serialize())


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


def get_compound_records_by_element(doc):
    """ Same as above but with element (removes the document merging logic)"""

    elements = doc.elements
    for el in elements:
        for record in el.records:
            print(record.serialize())


def get_table_records(doc):
    """ Function to extract the photovoltaic device information from tables.
        Returns a tuple of (pv_record, table) for each PhotovoltaicCell records that is determined.
        :param chemdataextractor.Document doc : Document used to extract
        :return Tuple(pv_record, chemdataextractor.table) tables_record : All Photovoltaic records

    """

    tables = doc.tables
    tables_records = []

    # Obtain the PhotovoltaicCell records from each table
    for table in tables:
        records = [record.serialize()['PhotovoltaicCell'] for record in table.records if 'PhotovoltaicCell' == record.__class__.__name__]
        for record in records:
            tables_records.append((record, table))

    # Remove results where the record is just one element long, or doesn't contain voc, jsc, ff or pce

    return tables_records


def add_dye_information(pv_records):
    """
    Function to add dye information from document if possible, following this logic:
    1) Check the table caption, using DyeSentence
    2) Check rest of document

    All these sections could begin with a search for compounds, and then follow this by a search for common dyes like N719...
    :return:
    """

    for pv_record in pv_records:
        pv_record.table.add_models([SentenceDye])

        if pv_record.dye is None:

            # Step 1: Check the caption using the DyeSentence parser
            # If found, this record is set with a 'contextual' flag to show that it was not taken directly from the table
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

            # Step 2: Check the rest of the document with the SentenceDye parser.
            # TODO: Extend this to check near vicinity first (ie areas in the doc that are nearby)
            # Then, look at the methods section
            # Then, if this fails, look at the most common specifier...?
            doc = pv_record.doc
            doc.add_models([SentenceDye])
            paragraphs = doc.paragraphs
            paragraph_records = [record.serialize() for paragraph in paragraphs for sentence in paragraph for record in sentence.records]
            for para_record in paragraph_records:

                if 'SentenceDye' in para_record.keys() and pv_record.dye is None:
                    para_record['SentenceDye']['contextual'] = 'sentence'
                    pv_record.dye = {'Dye': [para_record['SentenceDye']]}

                elif 'SentenceDye' in para_record.keys():
                    para_record['SentenceDye']['contextual'] = 'sentence'
                    pv_record.dye['Dye'].append(para_record['SentenceDye'])

    return pv_records






if __name__ == '__main__':
    create_dsscdb_from_file('/home/edward/pv/webscraping/rsc/articles/subset for development/C6RA14857C.html')

    # /home/edward/pv/webscraping/elsevier/articles/failed_training_downloads/S1385894717300542.xml')