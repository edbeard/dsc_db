"""
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""
import unittest
from dsc_db.run_perovskites import add_contextual_info, PerovskiteRecord, peroskite_material_properties

from chemdataextractor.doc.text import Caption, Paragraph
from chemdataextractor.doc import Document
from chemdataextractor.doc.table import Table
from chemdataextractor.model.pv_model import Perovskite, HoleTransportLayer, ElectronTransportLayer, PerovskiteSolarCell


class TestRunPerovskites(unittest.TestCase):

    def do_contextual_table_caption_merging(self, caption_text, model, expected):
        caption = Caption(caption_text)
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        pv_records = [PerovskiteRecord(pv_input, Table(caption, models=[model]))]
        filtered_elements = []
        pv_records = add_contextual_info(pv_records, filtered_elements, peroskite_material_properties)
        output = pv_records[0].serialize()
        self.assertEqual(output, expected)

    def do_contextual_document_merging(self, text, model, expected):
        filtered_elements = Paragraph(text)
        doc = Document(filtered_elements)
        doc.add_models([model])
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        pv_records = [PerovskiteRecord(pv_input, Table(Caption(''), models=[model]))]
        pv_records = add_contextual_info(pv_records, doc, peroskite_material_properties)
        output = pv_records[0].serialize()
        self.assertEqual(output, expected)

    def test_add_contextual_perovskite_from_table_caption_1(self):
        caption = 'This experiment was done with a perovskite of CH3NH3PbI3.'
        expected = {'perovskite': {'Perovskite': {'contextual': 'table_caption',
                               'raw_value': 'CH3NH3PbI3',
                               'specifier': 'perovskite'}},
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                'raw_value': '756',
                                'specifier': 'Voc',
                                'units': '(10^-3.0) * Volt^(1.0)',
                                'value': [756.0]}}}
        self.do_contextual_table_caption_merging(caption, Perovskite, expected)

    def test_add_contextual_perovskite_from_table_caption_2(self):
        caption = 'Summary of photovoltaic parameters of the fully-vacuum-processed perovskite solar cells using 5.5 nm' \
                  ' thick C60 ESLs, 370 nm thick CH3NH3PbI3 films and CuPc HSLs with different thicknesses measured under the reverse voltage scanning '
        expected = {'perovskite': {'Perovskite': {'contextual': 'table_caption',
                               'raw_value': 'CH3NH3PbI3',
                               'specifier': 'perovskite'}},
                'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                'raw_value': '756',
                                'specifier': 'Voc',
                                'units': '(10^-3.0) * Volt^(1.0)',
                                'value': [756.0]}}}
        self.do_contextual_table_caption_merging(caption, Perovskite, expected)


    def test_add_contextual_perovskite_from_context(self):
        sentence = 'CH3NH3PbI3 perovskite films were vacuum-deposited by heating CH3NH3I and PbI2 (Sigma, 99.999%) powder in two individual crucibles with the growth conditions of PbI2 rate at 0.75 Å s−1 and CH3NH3I pressure at 5 × 10−5 Torr.'
        expected = {'perovskite': {'Perovskite': {'contextual': 'document',
                               'raw_value': 'CH3NH3PbI3',
                               'specifier': 'perovskite'}},
        'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                'raw_value': '756',
                                'specifier': 'Voc',
                                'units': '(10^-3.0) * Volt^(1.0)',
                                'value': [756.0]}}}
        self.do_contextual_document_merging(sentence, Perovskite, expected)

    def test_add_contextual_htc_from_table_caption(self):
        caption = 'Summary of photovoltaic parameters of the fully-vacuum-processed perovskite solar cells using 5.5 nm thick C60 ESLs, 370 nm thick CH3NH3PbI3 films and CuPc HSLs with different thicknesses measured under the reverse voltage scanning.'
        expected = {'htl': {'HoleTransportLayer': {'contextual': 'table_caption',
                                'raw_value': 'CuPc',
                                'specifier': 'HSLs'}},
        'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                'raw_value': '756',
                                'specifier': 'Voc',
                                'units': '(10^-3.0) * Volt^(1.0)',
                                'value': [756.0]}}}

        self.do_contextual_table_caption_merging(caption, HoleTransportLayer, expected)

    def test_add_contextual_htc_from_context(self):
        caption = "Device parameters for MAPbI3 solar cells prepared on an identical TiO2 ETL and capped with a spiro-MeOTAD HTL."
        expected = {'htl': {'HoleTransportLayer': {'contextual': 'table_caption',
                                                   'raw_value': 'spiro - MeOTAD',
                                                   'specifier': 'HTL'}},
                    'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                   'raw_value': '756',
                                                   'specifier': 'Voc',
                                                   'units': '(10^-3.0) * Volt^(1.0)',
                                                   'value': [756.0]}}}
        self.do_contextual_table_caption_merging(caption, HoleTransportLayer, expected)

    def test_multiple_params_from_caption(self):
        caption = "Device parameters for MAPbI3 solar cells prepared on an identical TiO2 ETL and capped with a spiro-MeOTAD HTL."
        expected = {'htl': {'HoleTransportLayer': {'contextual': 'table_caption',
                                                   'raw_value': 'spiro - MeOTAD',
                                                   'specifier': 'HTL'}},
                    'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                   'raw_value': '756',
                                                   'specifier': 'Voc',
                                                   'units': '(10^-3.0) * Volt^(1.0)',
                                                   'value': [756.0]}}}
        self.do_contextual_table_caption_merging(caption, PerovskiteSolarCell, expected)



