"""
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""
import unittest
from dsc_db.run_perovskites import add_contextual_info, PerovskiteRecord, peroskite_material_properties, \
    enhance_common_values, get_filtered_elements, perovskite_properties, create_pdb_from_file

from chemdataextractor.doc.text import Caption, Paragraph
from chemdataextractor.doc import Document
from chemdataextractor.doc.table import Table
from chemdataextractor.model.pv_model import Perovskite, HoleTransportLayer, ElectronTransportLayer, \
    PerovskiteSolarCell, \
    SentencePerovskite, CounterElectrode, ActiveArea, Substrate
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

    def do_contextual_document_merging(self, text, model, expected, props=peroskite_material_properties):
        filtered_elements = Paragraph(text)
        doc = Document(filtered_elements)
        doc.add_models([model])
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        pv_records = [PerovskiteRecord(pv_input, Table(Caption(''), models=[model]))]
        pv_records = add_contextual_info(pv_records, doc, props)
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
        self.do_contextual_table_caption_merging(caption, SentencePerovskite, expected)

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
        self.do_contextual_table_caption_merging(caption, SentencePerovskite, expected)

    def test_add_contextual_perovskite_from_document(self):
        sentence = 'CH3NH3PbI3 perovskite films were vacuum-deposited by heating CH3NH3I and PbI2 (Sigma, 99.999%) powder in two individual crucibles with the growth conditions of PbI2 rate at 0.75 Å s−1 and CH3NH3I pressure at 5 × 10−5 Torr.'
        expected = {'perovskite': {'Perovskite': {'contextual': 'document',
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
        expected = {'perovskite': {'Perovskite': {'contextual': 'document',
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

    def test_add_contextual_etc_from_document_2(self):
        text = "Fig. 1c and d show the J–V characteristics of the two (representative) devices fabricated using PC61BM as EELs, before and after light soaking. "
        expected = {'etl': {'ElectronTransportLayer': {'contextual': 'document',
                                                       'labels': ['phenyl-C61-butyric acid methyl '
                                                                  'ester',
                                                                  'PCBM',
                                                                  'PC60BM',
                                                                  'PC61BM'],
                                                       'name': 'phenyl-C61-butyric acid methyl '
                                                               'ester',
                                                       'raw_value': 'PC61BM',
                                                       'specifier': 'EELs'}},
                    'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                   'raw_value': '756',
                                                   'specifier': 'Voc',
                                                   'units': '(10^-3.0) * Volt^(1.0)',
                                                   'value': [756.0]}}}
        filtered_elements = Paragraph(text)
        doc = Document(filtered_elements)
        doc.add_models([ElectronTransportLayer])
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        pv_records = [PerovskiteRecord(pv_input, Table(Caption(''), models=[ElectronTransportLayer]))]
        pv_records = add_contextual_info(pv_records, doc, peroskite_material_properties)
        pv_records = enhance_common_values(pv_records)
        output = pv_records[0].serialize()

        self.assertEqual(output, expected)

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
                                   'formula': '(CH3NH3)PbCl3',
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
                                                          'PCBM',
                                                          'PC60BM',
                                                          'PC61BM'],
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
                                           'smiles': {'context': 'dict',
                                                      'value': 'CSc1ccc(cc1)N(c2ccc(SC)cc2)c3ccc4c5ccc(cc5C6(c4c3)c7cc(ccc7c8ccc(cc68)N(c9ccc(SC)cc9)c%10ccc(SC)cc%10)N(c%11ccc(SC)cc%11)c%12ccc(SC)cc%12)N(c%13ccc(SC)cc%13)c%14ccc(SC)cc%14'}}}

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
                                           'smiles': {'context': 'dict',
                                                      'value': 'COC1=CC=C(C=C1)N(C2=CC=C(C=C2)OC)C3=CC4=C(C=C3)C5=C(C46C7=CC=CC=C7OC8=CC=CC=C68)C=C(C=C5)N(C9=CC=C(C=C9)OC)C1=CC=C(C=C1)OC'}}}
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
                                   'formula': '(CH3NH3)PbCl3',
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
                                   'formula': '((C4H11N))2((CH3NH3))n-1PbnI3n+1',
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

    def test_counter_electrode_extraction(self):
        sentence = 'Herein, we demonstrated a low temperature solution process to obtain high quality CsPbI2Br films and fabricate devices with a facile n-i-p structure (ITO/SnO2/CsPbI2Br/Spiro-OMeTAD/MoO3/Ag), in which MoO3 was introduced as interfacial layer that led to high efficient charge extraction and suppressed carrier recombination.'
        expected = {'counter_electrode': {'CounterElectrode': {'contextual': 'document',
                                                               'raw_value': 'Ag',
                                                               'specifier': 'ITO'}},
                    'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                   'raw_value': '756',
                                                   'specifier': 'Voc',
                                                   'units': '(10^-3.0) * Volt^(1.0)',
                                                   'value': [756.0]}}}
        self.do_contextual_document_merging(sentence, CounterElectrode, expected, props=perovskite_properties)

    def test_etl_thickness_extraction(self):
        sentence = ' For the preparation of 60 nm thick compact TiO2 layer, a precursor solution was prepared by adding 1 mL titanium diisopropoxide bis(acetylacetonate) (Sigma–Aldrich) into 39 mL absolute ethanol. '
        pass

    def test_active_area_extraction(self):
        sentence = 'The active area of all devices was defined as 0.16 cm2.'
        expected = {'active_area': {'ActiveArea': {'contextual': 'document',
                                                   'raw_units': 'cm2',
                                                   'raw_value': '0.16',
                                                   'specifier': 'active area',
                                                   'std_units': 'Meter^(2.0)',
                                                   'std_value': [1.6e-05],
                                                   'units': '(10^-4.0) * Meter^(2.0)',
                                                   'value': [0.16]}},
                    'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                   'raw_value': '756',
                                                   'specifier': 'Voc',
                                                   'units': '(10^-3.0) * Volt^(1.0)',
                                                   'value': [756.0]}}}
        self.do_contextual_document_merging(sentence, ActiveArea, expected, props=perovskite_properties)

    def test_active_area_extraction_2(self):
        sentence = 'The total active area of the semi-transparent cells is 0.3 cm2'
        expected = {'active_area': {'ActiveArea': {'contextual': 'document',
                                                   'raw_units': 'cm2',
                                                   'raw_value': '0.3',
                                                   'specifier': 'active area',
                                                   'std_units': 'Meter^(2.0)',
                                                   'std_value': [3e-05],
                                                   'units': '(10^-4.0) * Meter^(2.0)',
                                                   'value': [0.3]}},
                    'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                   'raw_value': '756',
                                                   'specifier': 'Voc',
                                                   'units': '(10^-3.0) * Volt^(1.0)',
                                                   'value': [756.0]}}}
        self.do_contextual_document_merging(sentence, ActiveArea, expected, props=perovskite_properties)

    def test_substrate_extraction(self):
        sentence = 'The peak marked “*” was the Indium tin oxide (ITO) substrate.'
        expected = {'substrate': {'Substrate': {'contextual': 'document',
                                                'raw_value': 'Indium tin oxide',
                                                'specifier': 'substrate'}},
                    'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                   'raw_value': '756',
                                                   'specifier': 'Voc',
                                                   'units': '(10^-3.0) * Volt^(1.0)',
                                                   'value': [756.0]}}}
        self.do_contextual_document_merging(sentence, Substrate, expected, props=perovskite_properties)

    def test_reference_contextual_filtering(self):
        table_input = [['Perovskite', 'Jsc (mA cm−2)', 'Voc (V)', 'FF', 'PCE', 'Ref'],
                       ['MAPbI3', '11.11', '22.22', '33.33', '44.44', '56']]
        input_table = Table(caption=Caption('Photovoltaic parameters for cells with the HTL Spiro-OMeTAD.'),
                            table_data=table_input)
        doc = Document(
            'It was found for some of these that the ETL was TiO2. For a specific case there was also a counter electrode, Ag.',
            input_table)
        pv_records = create_pdb_from_file(doc)
        expected = {'derived_properties': {'solar_simulator': {'error': 2.0,
                                                               'units': 'WattPerMeterSquared^(1.0)',
                                                               'value': [1851.0]}},
                    'ff': {'FillFactor': {'raw_value': '33.33',
                                          'specifier': 'FF',
                                          'value': [33.33]}},
                    'htl': {'HoleTransportLayer': {'contextual': 'table_caption',
                                                   'labels': ['Spiro-OMeTAD',
                                                              'SpiroOMeTAD',
                                                              "2,2',7,7'-Tetrakis-(N,N-di-4-methoxyphenylamino)-9,9'-spirobifluorene",
                                                              'C81H68N4O8',
                                                              'Spiro-MeOTAD',
                                                              'SpiroMeOTAD',
                                                              'N7′-octakis(4-methoxyphenyl)-9,9′-spirobi[9H-fluorene]-2,2′,7,7′-tetramine',
                                                              'pp-Spiro-OMeTAD'],
                                                   'name': "2,2',7,7'-Tetrakis-(N,N-di-4-methoxyphenylamino)-9,9'-spirobifluorene",
                                                   'raw_value': 'Spiro - OMeTAD',
                                                   'smiles': {'context': 'dict',
                                                              'value': 'COC1=CC=C(C=C1)N(C2=CC=C(C=C2)OC)C3=CC4=C(C=C3)C5=C(C46C7=C(C=CC(=C7)N(C8=CC=C(C=C8)OC)C9=CC=C(C=C9)OC)C1=C6C=C(C=C1)N(C1=CC=C(C=C1)OC)C1=CC=C(C=C1)OC)C=C(C=C5)N(C1=CC=C(C=C1)OC)C1=CC=C(C=C1)OC'},
                                                   'specifier': 'HTL'}},
                    'jsc': {'ShortCircuitCurrentDensity': {'raw_units': '(mAcm−2)',
                                                           'raw_value': '11.11',
                                                           'specifier': 'Jsc',
                                                           'std_units': 'Ampere^(1.0)  '
                                                                        'Meter^(-2.0)',
                                                           'std_value': [111.1],
                                                           'units': '(10^1.0) * Ampere^(1.0)  '
                                                                    'Meter^(-2.0)',
                                                           'value': [11.11]}},
                    'pce': {'PowerConversionEfficiency': {'raw_value': '44.44',
                                                          'specifier': 'PCE',
                                                          'value': [44.44]}},
                    'perovskite': {'Perovskite': {'formula': '(CH3NH3)PbI3',
                                                  'raw_value': 'MAPbI3',
                                                  'specifier': 'Perovskite'}},
                    'ref': {'Reference': {'raw_value': '56', 'specifier': 'Ref', 'value': [56.0]}},
                    'solar_simulator': {'SimulatedSolarLightIntensity': {'derived_error': 2.0,
                                                                         'derived_units': 'WattPerMeterSquared^(1.0)',
                                                                         'derived_value': [1851.0]}},
                    'table_row_categories': 'MAPbI3',
                    'voc': {'OpenCircuitVoltage': {'raw_units': '(V)',
                                                   'raw_value': '22.22',
                                                   'specifier': 'Voc',
                                                   'std_units': 'Volt^(1.0)',
                                                   'std_value': [22.22],
                                                   'units': 'Volt^(1.0)',
                                                   'value': [22.22]}}}

        output = pv_records[0].serialize()

        self.assertEqual(expected, output)
        self.assertFalse('etl' in output.keys())
        self.assertFalse('counter_electrode' in output.keys())

    def test_merging_of_contextual_spiroometad(self):
        """
        Add test for merging case of spiro - OMeTAD.
        In document 10.1016:j.electacta.2015.10.030.json
        """
        text = "A cells used a HTL consisting of spiro-OMeTAD. "
        expected = {'htl': {'HoleTransportLayer': {'contextual': 'document',
                                                   'labels': ['Spiro-OMeTAD',
                                                              'SpiroOMeTAD',
                                                              "2,2',7,7'-Tetrakis-(N,N-di-4-methoxyphenylamino)-9,9'-spirobifluorene",
                                                              'C81H68N4O8',
                                                              'Spiro-MeOTAD',
                                                              'SpiroMeOTAD',
                                                              'N7′-octakis(4-methoxyphenyl)-9,9′-spirobi[9H-fluorene]-2,2′,7,7′-tetramine',
                                                              'pp-Spiro-OMeTAD'],
                                                   'name': "2,2',7,7'-Tetrakis-(N,N-di-4-methoxyphenylamino)-9,9'-spirobifluorene",
                                                   'raw_value': 'spiro - OMeTAD',
                                                   'smiles': {'context': 'dict',
                                                              'value': 'COC1=CC=C(C=C1)N(C2=CC=C(C=C2)OC)C3=CC4=C(C=C3)C5=C(C46C7=C(C=CC(=C7)N(C8=CC=C(C=C8)OC)C9=CC=C(C=C9)OC)C1=C6C=C(C=C1)N(C1=CC=C(C=C1)OC)C1=CC=C(C=C1)OC)C=C(C=C5)N(C1=CC=C(C=C1)OC)C1=CC=C(C=C1)OC'},
                                                   'specifier': 'HTL'}},
                    'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                   'raw_value': '756',
                                                   'specifier': 'Voc',
                                                   'units': '(10^-3.0) * Volt^(1.0)',
                                                   'value': [756.0]}}}
        filtered_elements = Paragraph(text)
        doc = Document(filtered_elements)
        doc.add_models([HoleTransportLayer])
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        pv_records = [PerovskiteRecord(pv_input, Table(Caption(''), models=[ElectronTransportLayer]))]
        pv_records = add_contextual_info(pv_records, doc, peroskite_material_properties)
        pv_records = enhance_common_values(pv_records)
        output = pv_records[0].serialize()

        self.assertEqual(output, expected)

    def test_merging_of_contextual_pedotpss(self):
        """
        Add test for merging case of spiro - OMeTAD.
        In document 10.1016:j.electacta.2015.10.030.json
        """
        text = "A cells used a HTL of PEDOT:PSS. "
        expected = {'htl': {'HoleTransportLayer': {'contextual': 'document',
                                                   'labels': ['PEDOT:PSS',
                                                              'poly(3,4-ethylenedioxythiophene) '
                                                              'polystyrene sulfonate'],
                                                   'name': 'poly(3,4-ethylenedioxythiophene) '
                                                           'polystyrene sulfonate',
                                                   'raw_value': 'PEDOT : PSS',
                                                   'smiles': {'context': 'dict', 'value': ''},
                                                   'specifier': 'HTL'}},
                    'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                   'raw_value': '756',
                                                   'specifier': 'Voc',
                                                   'units': '(10^-3.0) * Volt^(1.0)',
                                                   'value': [756.0]}}}
        filtered_elements = Paragraph(text)
        doc = Document(filtered_elements)
        doc.add_models([HoleTransportLayer])
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        pv_records = [PerovskiteRecord(pv_input, Table(Caption(''), models=[ElectronTransportLayer]))]
        pv_records = add_contextual_info(pv_records, doc, peroskite_material_properties)
        pv_records = enhance_common_values(pv_records)
        output = pv_records[0].serialize()

        self.assertEqual(output, expected)