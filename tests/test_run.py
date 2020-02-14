"""
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import unittest

from dsc_db.model import PhotovoltaicRecord
from dsc_db.run import add_dye_information

from chemdataextractor import Document
from chemdataextractor.model import Compound
from chemdataextractor.model.pv_model import PhotovoltaicCell, SentenceDye
from chemdataextractor.doc import Table, Caption, Paragraph


class TestRun(unittest.TestCase):

    def test_dye_candidate_caption_substitution(self):
        """ Test the case where dye is specified in the caption"""
        table_input = [['CE',	'Jsc (mA cm−2)', 'Voc (V)', 'FF', 'PCE'], ['Pt', '11.11', '22.22', '33.33', '44.44']]
        input_table = Table(caption=Caption('Photovoltaic parameters for cells with the sensitizer N719.', table_data=table_input))
        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        doc = Document('Null', input_table)
        doc.add_models([PhotovoltaicCell, Compound, SentenceDye])
        pv_records = [PhotovoltaicRecord(input, input_table)]
        pv_records = add_dye_information(pv_records, doc)
        self.assertEqual(pv_records[0].dye, {'Dye': [{'contextual': 'table', 'raw_value': 'N719', 'specifier': 'sensitizer'}]})

    def test_dye_candidate_document_substitution(self):
        """ Test the case where dye is specified in the document"""
        table_input = [['CE',	'Jsc (mA cm−2)', 'Voc (V)', 'FF', 'PCE'], ['Pt', '11.11', '22.22', '33.33', '44.44']]
        table = Table(caption=Caption('Null'), table_data=table_input)#, models=[PhotovoltaicCell])
        input_doc = Document(Paragraph('This is a test document. It says a few cool things. It also defines the dye, X23'), table)
        input_doc.add_models([PhotovoltaicCell, Compound, SentenceDye])
        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        pv_records = [PhotovoltaicRecord(input, table)]
        pv_records = add_dye_information(pv_records, input_doc)
        self.assertEqual({'Dye': [{'contextual': 'document', 'raw_value': 'X23', 'specifier': 'dye'}]}, pv_records[0].dye)

    def test_dye_candidate_document_substitution_with_compound_substitution(self):
        table_input = [['CE',	'Jsc (mA cm−2)', 'Voc (V)', 'FF', 'PCE'], ['Pt', '11.11', '22.22', '33.33', '44.44']]
        table = Table(caption=Caption('Null'), table_data=table_input)
        para = Paragraph("Organic sensitizer of 3-{6-{4-[bis(2′,4′-dihexyloxybiphenyl-4-yl)amino-]phenyl}-4,4-dihexyl-cyclopenta-[2,1-b:3,4-b']dithiophene-2-yl}-2-cyanoacrylic acid (Y123) was purchased from Dyenamo and used without purification.")
        input_doc = Document(para, table)

        input_doc.add_models([PhotovoltaicCell, Compound, SentenceDye])
        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        expected = {'Dye': [{'specifier': 'sensitizer', 'raw_value': 'Y123', 'contextual': 'document',
                    'compound': {'names': ["3-{6-{4-[bis(2′,4′-dihexyloxybiphenyl-4-yl)amino-]phenyl}-4,4-dihexyl-cyclopenta-[2,1-b:3,4-b']dithiophene-2-yl}-2-cyanoacrylic acid"], 'labels': ['Y123']}}]}

        pv_records = [PhotovoltaicRecord(input, Table(caption=Caption('Null')))]
        pv_records = add_dye_information(pv_records, input_doc)

        doc_records = [record.serialize() for record in input_doc.records]
        compound_records = [record['Compound'] for record in doc_records if 'Compound' in record.keys()]
        for pv_record in pv_records:
            if pv_record.dye is not None:
                pv_record._substitute_compound('dye', 'Dye', compound_records)

        self.assertEqual(pv_records[0].dye, expected)

    def test_dye_candidate_document_substitution_with_abbreviation_substitution(self):
        input_table = Table(caption=Caption('Photovoltaic parameters for cells with the sensitizer N719.'))
        input_para = Paragraph('Here is a definition: N719 = not-my-real-name 719 ')

        input_doc = Document(input_para, input_table)
        input_doc.add_models([PhotovoltaicCell, Compound, SentenceDye])

        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        expected = {'Dye': [   {   'abbreviations': [['not-my-real-name', '719']],
                              'contextual': 'table',
                              'raw_value': 'N719',
                              'specifier': 'sensitizer'}]}

        pv_records = [PhotovoltaicRecord(input, input_table)]
        pv_records = add_dye_information(pv_records, input_doc)

        for pv_record in pv_records:
            if pv_record.dye is not None:
                pv_record._substitute_definitions('dye', 'Dye', input_doc)

        self.assertEqual(pv_records[0].dye, expected)



