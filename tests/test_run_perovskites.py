"""
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""
import unittest
from dsc_db.run_perovskites import add_contextual_info, PerovskiteRecord, peroskite_material_properties, \
    enhance_common_values, get_filtered_elements

from chemdataextractor.doc.text import Caption, Paragraph
from chemdataextractor.doc import Document
from chemdataextractor.doc.table import Table
from chemdataextractor.model.pv_model import Perovskite, HoleTransportLayer, ElectronTransportLayer, PerovskiteSolarCell, SentencePerovskite
from chemdataextractor.model import Compound


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
        expected = {'perovskite': {'SentencePerovskite': {'contextual': 'table_caption',
                               'raw_value': 'CH3NH3PbI3',
                               'specifier': 'perovskite'}},
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                'raw_value': '756',
                                'specifier': 'Voc',
                                'units': '(10^-3.0) * Volt^(1.0)',
                                'value': [756.0]}}}
        self.do_contextual_table_caption_merging(caption, SentencePerovskite, expected)

    def test_add_contextual_perovskite_from_table_caption_2(self):
        caption = 'Summary of photovoltaic parameters of the fully-vacuum-processed perovskite solar cells using 5.5 nm' \
                  ' thick C60 ESLs, 370 nm thick CH3NH3PbI3 films and CuPc HSLs with different thicknesses measured under the reverse voltage scanning '
        expected = {'perovskite': {'SentencePerovskite': {'contextual': 'table_caption',
                               'raw_value': 'CH3NH3PbI3',
                               'specifier': 'perovskite'}},
                'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                'raw_value': '756',
                                'specifier': 'Voc',
                                'units': '(10^-3.0) * Volt^(1.0)',
                                'value': [756.0]}}}
        self.do_contextual_table_caption_merging(caption, SentencePerovskite, expected)

    def test_add_contextual_perovskite_from_document(self):
        sentence = 'CH3NH3PbI3 perovskite films were vacuum-deposited by heating CH3NH3I and PbI2 (Sigma, 99.999%) powder in two individual crucibles with the growth conditions of PbI2 rate at 0.75 Å s−1 and CH3NH3I pressure at 5 × 10−5 Torr.'
        expected = {'perovskite': {'SentencePerovskite': {'contextual': 'document',
                               'raw_value': 'CH3NH3PbI3',
                               'specifier': 'perovskite'}},
        'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                'raw_value': '756',
                                'specifier': 'Voc',
                                'units': '(10^-3.0) * Volt^(1.0)',
                                'value': [756.0]}}}
        self.do_contextual_document_merging(sentence, SentencePerovskite, expected)

    def test_add_contextual_perovskite_from_document_2(self):
        sentence = 'On exposure to light, charge carriers are generated in the MAPbI3 perovskite photoactive layer, and electrons and holes are subsequently extracted and collected by their respective contacts, ETL and HTL.'
        expected = {'perovskite': {'SentencePerovskite': {'contextual': 'document',
                               'raw_value': 'MAPbI3',
                               'specifier': 'perovskite'}},
        'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                'raw_value': '756',
                                'specifier': 'Voc',
                                'units': '(10^-3.0) * Volt^(1.0)',
                                'value': [756.0]}}}
        self.do_contextual_document_merging(sentence, SentencePerovskite, expected)

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

    def test_add_contextual_htc_from_document(self):
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

    def test_add_contextual_htc_from_document_2(self):
        caption = "Device parameters for MAPbI3 solar cells prepared on an identical TiO2 ETL and capped with a Spiro-S HTL."
        expected = {'htl': {'HoleTransportLayer': {'contextual': 'table_caption',
                                                   'raw_value': 'Spiro-S',
                                                   'specifier': 'HTL'}},
                    'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                   'raw_value': '756',
                                                   'specifier': 'Voc',
                                                   'units': '(10^-3.0) * Volt^(1.0)',
                                                   'value': [756.0]}}}
        self.do_contextual_table_caption_merging(caption, HoleTransportLayer, expected)

    def test_add_contextual_etc_from_document(self):
        text = "The device used c-TiO2 in the electron transport layer."
        expected = {'etl': {'ElectronTransportLayer': {'contextual': 'document',
                                    'raw_value': 'c-TiO2',
                                    'specifier': 'electron transport layer'}},
                'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                'raw_value': '756',
                                'specifier': 'Voc',
                                'units': '(10^-3.0) * Volt^(1.0)',
                                'value': [756.0]}}}
        self.do_contextual_document_merging(text, ElectronTransportLayer, expected)

    def test_multiple_params_from_caption(self):
        caption = "Device parameters for MAPbI3 solar cells prepared on an identical TiO2 ETL and capped with a spiro-MeOTAD HTL."
        expected = {'etl': {'ElectronTransportLayer': {'contextual': 'table_caption',
                                    'raw_value': 'TiO2',
                                    'specifier': 'ETL'}},
                     'htl': {'HoleTransportLayer': {'contextual': 'table_caption',
                                                    'raw_value': 'spiro - MeOTAD',
                                                    'specifier': 'HTL'}},
                     'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                'raw_value': '756',
                                                'specifier': 'Voc',
                                                'units': '(10^-3.0) * Volt^(1.0)',
                                                'value': [756.0]}}}
        self.do_contextual_table_caption_merging(caption, PerovskiteSolarCell, expected)


    ### Testing the addition of information for common Perovskites

    def test_enhance_common_values_perovskite(self):
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'perovskite': {'Perovskite': {'contextual': 'document', 'raw_value': 'MAPbCl3'}}
        }

        expected = {'Perovskite': {'contextual': 'document',
                'formula': 'CH3NH3PbCl3',
                'raw_value': 'MAPbCl3'}}

        pv_records = [PerovskiteRecord(pv_input, Table(Caption('')))]
        pv_records = enhance_common_values(pv_records)
        self.assertEqual(pv_records[0].perovskite, expected)

    def test_enhance_common_values_hole_transporting_layer(self):
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'htl': {'HoleTransportLayer': {'contextual': 'document', 'raw_value': 'EH44'}}
        }

        expected = {'HoleTransportLayer': {'contextual': 'document',
                        'labels': ['EH44',
                                   '9-(2-Ethylhexyl)-N,N,N,N-tetrakis(4-methoxyphenyl)- '
                                   '9H-carbazole-2,7-diamine)',
                                   'C48H51N3O4'],
                        'name': '9-(2-Ethylhexyl)-N,N,N,N-tetrakis(4-methoxyphenyl)- '
                                '9H-carbazole-2,7-diamine)',
                        'raw_value': 'EH44',
                        'smiles': {'context': 'dict', 'value': ''}}}

        pv_records = [PerovskiteRecord(pv_input, Table(Caption('')))]
        pv_records = enhance_common_values(pv_records)
        self.assertEqual(pv_records[0].htl, expected)

    def test_enhance_common_values_electron_transporting_layer(self):
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'etl': {'ElectronTransportLayer': {'contextual': 'document', 'raw_value': 'PCBM'}}
        }

        expected = {'ElectronTransportLayer': {'contextual': 'document',
                            'labels': ['phenyl-C61-butyric acid methyl ester',
                                       'PCBM'],
                            'name': 'phenyl-C61-butyric acid methyl ester',
                            'raw_value': 'PCBM'}}

        pv_records = [PerovskiteRecord(pv_input, Table(Caption('')))]
        pv_records = enhance_common_values(pv_records)
        self.assertEqual(pv_records[0].etl, expected)

    def test_enhance_common_values_electron_transporting_layer_with_structure_field(self):
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'etl': {'ElectronTransportLayer': {'contextual': 'document', 'raw_value': 'c-TiO2'}}
        }

        expected = {'ElectronTransportLayer': {'contextual': 'document',
                            'labels': ['c-TiO2', 'compact titanium dioxide'],
                            'name': 'titanium dioxide',
                            'raw_value': 'c-TiO2',
                            'structure': 'compact'}}

        pv_records = [PerovskiteRecord(pv_input, Table(Caption('')))]
        pv_records = enhance_common_values(pv_records)
        self.assertEqual(pv_records[0].etl, expected)

    def test_enhance_common_values_etl_1(self):
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'etl': {'ElectronTransportLayer': {'contextual': 'document', 'raw_value': 'Zirconium Dioxide'}}
        }
        expected = {'ElectronTransportLayer': {'contextual': 'document',
                            'raw_value': 'Zirconium Dioxide',
                             'labels': ['zirconium dioxide', 'ZrO2'],
                             'name': 'zirconium dioxide'}}
        pv_records = [PerovskiteRecord(pv_input, Table(Caption('')))]
        pv_records = enhance_common_values(pv_records)
        self.assertEqual(expected, pv_records[0].etl)

    def test_enhance_common_values_etl_2(self):
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'etl': {'ElectronTransportLayer': {'contextual': 'document', 'raw_value': 'WO3 / TiO2'}}
        }
        expected = {'ElectronTransportLayer': {'contextual': 'document',
                            'raw_value': 'WO3 / TiO2',
                     'labels': ['WO3/TiO2'],
                     'name': 'tungsten trioxide / titanium dioxide',
                     'structure': 'core-shell'}}
        pv_records = [PerovskiteRecord(pv_input, Table(Caption('')))]
        pv_records = enhance_common_values(pv_records)
        self.assertEqual(expected, pv_records[0].etl)

    def test_enhance_common_values_htl_1(self):
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'htl': {'HoleTransportLayer': {'contextual': 'document', 'raw_value': 'Spiro-S'}}
        }
        expected = {'HoleTransportLayer': {'contextual': 'document', 'raw_value': 'Spiro-S',
            'labels': ['Spiro-S',
                    '2,2′,7,7′-tetrakis[N,N-bis(p-methylsulfanylphenyl)amino]-9,9′-spirobifluorene'],
            'name': '2,2′,7,7′-tetrakis[N,N-bis(p-methylsulfanylphenyl)amino]-9,9′-spirobifluorene',
            'smiles': {'context':'dict', 'value':'CSc1ccc(cc1)N(c2ccc(SC)cc2)c3ccc4c5ccc(cc5C6(c4c3)c7cc(ccc7c8ccc(cc68)N(c9ccc(SC)cc9)c%10ccc(SC)cc%10)N(c%11ccc(SC)cc%11)c%12ccc(SC)cc%12)N(c%13ccc(SC)cc%13)c%14ccc(SC)cc%14'}}}

        pv_records = [PerovskiteRecord(pv_input, Table(Caption('')))]
        pv_records = enhance_common_values(pv_records)
        self.assertEqual(expected, pv_records[0].htl)

    def test_enhance_common_values_htl_2(self):
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'htl': {'HoleTransportLayer': {'contextual': 'document', 'raw_value': 'X59'}}
        }
        expected = {'HoleTransportLayer': {'contextual': 'document', 'raw_value': 'X59',
                        'labels': ['X59',
                                'Spiro[9H-fluorene-9,9′-[9H]xanthene]-2,7-diamine',
                                'N,N,N′,N′-tetrakis(4-methoxyphenyl)spiro[fluorene-9,9′-xanthene]-2,7-diamine',
                                "2-N,2-N,7-N,7-N-tetrakis(4-methoxyphenyl)spiro[fluorene-9,9'-xanthene]-2,7-diamine",
                                'N′,N′,N′′,N′′-tetrakis(4-methoxyphenyl)spiro[fluorene-9,9′-xanthene]−2,7-diamineC53H42N2O5'],
                        'name': "2-N,2-N,7-N,7-N-tetrakis(4-methoxyphenyl)spiro[fluorene-9,9'-xanthene]-2,7-diamine",
                        'smiles': {'context':'dict', 'value':'COC1=CC=C(C=C1)N(C2=CC=C(C=C2)OC)C3=CC4=C(C=C3)C5=C(C46C7=CC=CC=C7OC8=CC=CC=C68)C=C(C=C5)N(C9=CC=C(C=C9)OC)C1=CC=C(C=C1)OC'}}}
        pv_records = [PerovskiteRecord(pv_input, Table(Caption('')))]
        pv_records = enhance_common_values(pv_records)
        self.assertEqual(expected, pv_records[0].htl)

    def test_enhance_common_substring_perovskite(self):
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'perovskite': {'Perovskite': {'contextual': 'document', 'raw_value': 'MAPbCl3'}}
        }
        expected = {'Perovskite': {'contextual': 'document',
                'formula': 'CH3NH3PbCl3',
                'raw_value': 'MAPbCl3'}}
        pv_records = [PerovskiteRecord(pv_input, Table(Caption('')))]
        pv_records = enhance_common_values(pv_records)
        self.assertEqual(expected, pv_records[0].perovskite)

    def test_enhance_common_substring_perovskite_2(self):
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'perovskite': {'Perovskite': {'contextual': 'document', 'raw_value': '(BA)2(MA)n-1PbnI3n+1'}}
        }
        expected = {'Perovskite': {'contextual': 'document',
                'formula': '(C4H11N)2(CH3NH3)n-1PbnI3n+1',
                'raw_value': '(BA)2(MA)n-1PbnI3n+1'}}
        pv_records = [PerovskiteRecord(pv_input, Table(Caption('')))]
        pv_records = enhance_common_values(pv_records)
        self.assertEqual(expected, pv_records[0].perovskite)

    def test_enhance_common_substring_perovskite_3(self):
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'perovskite': {'Perovskite': {'contextual': 'document', 'raw_value': 'RbPbBr3'}}
        }
        expected = {'Perovskite': {'contextual': 'document',
                'formula': 'RbPbBr3',
                'raw_value': 'RbPbBr3'}}
        pv_records = [PerovskiteRecord(pv_input, Table(Caption('')))]
        pv_records = enhance_common_values(pv_records)
        self.assertEqual(expected, pv_records[0].perovskite)
