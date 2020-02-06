"""
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import unittest

from dsc_db.model import PhotovoltaicRecord
from dsc_db.run import add_dye_information
from pprint import pprint

from chemdataextractor import Document
from chemdataextractor.doc import Table, Caption


class TestRun(unittest.TestCase):

    def test_dye_candidate_caption_substitution(self):
        """ Test the case where dye is specified in the caption"""
        input_table = Table(caption=Caption('Photovoltaic parameters for cells with the sensitizer N719.'))
        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        pv_records = [PhotovoltaicRecord(input, Document('Null'), input_table)]
        pv_records = add_dye_information(pv_records)
        self.assertEqual(pv_records[0].dye, {'Dye': [{'contextual': 'table', 'raw_value': 'N719', 'specifier': 'sensitizer'}]})

    def test_dye_candidate_document_substitution(self):
        """ Test the case where dye is specified in the document"""
        input_doc = Document('This is a test document. It says a few cool things. It also defines the dye, X23')
        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        pv_records = [PhotovoltaicRecord(input, input_doc, Table(caption=Caption('Null')))]
        pv_records = add_dye_information(pv_records)
        self.assertEqual(pv_records[0].dye, {'Dye': [{'contextual': 'sentence', 'raw_value': 'X23', 'specifier': 'dye'}]})

