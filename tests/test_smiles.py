"""
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import unittest

from chemdataextractor.doc import Table, Caption

from dsc_db.smiles import get_smiles_pubchem, add_smiles, add_smiles_perovskite_htl
from dsc_db.model import PhotovoltaicRecord, PerovskiteRecord


class TestSmiles(unittest.TestCase):

    def do_smiles_test(self):
        pass

    def test_pubchem_smiles(self):
        name = 'glucose'
        smiles = get_smiles_pubchem(name)
        self.assertEqual(smiles, ['C([C@@H]1[C@H]([C@@H]([C@H](C(O1)O)O)O)O)O'])

    def test_compound_record_substitution(self):
        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'dye': {'Dye': [{'raw_value': 'glucose', 'specifier': 'dye',
                             'compound': {'names': ["glucose"], 'labels': ['Y123']}}]}
        }
        expected = {
            'Dye': [
                {'raw_value': 'glucose', 'specifier': 'dye', 'compound': {'names': ['glucose'], 'labels': ['Y123']},
                 'smiles': {'value': 'C([C@@H]1[C@H]([C@@H]([C@H](C(O1)O)O)O)O)O', 'context': 'compound'}}]}

        pv_records = [PhotovoltaicRecord(input, Table(Caption("")))]
        pv_records = add_smiles(pv_records)
        self.assertEqual(pv_records[0].dye, expected)

    def test_abbreviations_record_substitution(self):

        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'dye': {'Dye': [{'abbreviations': [['sodium', 'chloride']], 'raw_value': 'table salt', 'specifier': 'dye',
                             }]
                    }
        }
        expected = {
            'Dye': [{'abbreviations': [['sodium', 'chloride']],
            'raw_value': 'table salt',
            'smiles': {'value': '[Na+].[Cl-]', 'context': 'abbreviation'},
            'specifier': 'dye'}]
        }

        pv_records = [PhotovoltaicRecord(input, Table(Caption("")))]
        pv_records = add_smiles(pv_records)
        self.assertEqual(pv_records[0].dye, expected)

    def test_raw_value_substitution(self):

        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'dye': {'Dye': [{'raw_value': 'butane', 'specifier': 'dye'
                             }]
                    }
        }

        expected = {'Dye': [{'raw_value': 'butane', 'smiles': {'value': 'CCCC', 'context': 'raw_value'}, 'specifier': 'dye'}]}

        pv_records = [PhotovoltaicRecord(input, Table(Caption("")))]
        pv_records = add_smiles(pv_records)
        self.assertEqual(pv_records[0].dye, expected)

    def test_abbr_substituted_before_compound(self):

        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'dye': {'Dye': [{'raw_value': 'C4H10', 'specifier': 'dye', 'compound': {'names': ['mis-assigned_name'], 'labels': ['ABC']},
                             'abbreviations': [['butane']]
                             }]
                    }
        }

        expected = {'Dye': [{'abbreviations': [['butane']],
          'compound': {'labels': ['ABC'], 'names': ['mis-assigned_name']},
          'raw_value': 'C4H10',
          'smiles': {'value':'CCCC', 'context': 'abbreviation'},
          'specifier': 'dye'}]}

        pv_records = [PhotovoltaicRecord(input, Table(Caption("")))]
        pv_records = add_smiles(pv_records)
        self.assertEqual(pv_records[0].dye, expected)

    def test_smiles_perovskite_htl_from_abbreviation(self):

        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'htl': {'HoleTransportLayer': {'abbreviations': [['Copper(I) thiocyanate']],
                                            'raw_value': 'CuSCN',
                                            'specifier': 'HTL'}}
        }

        expected = {'HoleTransportLayer': {'abbreviations': [['Copper(I) thiocyanate']],
                        'raw_value': 'CuSCN',
                        'smiles': {'context': 'abbreviation',
                                   'value': 'C(#N)[S-].[Cu+]'},
                        'specifier': 'HTL'}}

        pv_records = [PerovskiteRecord(input, Table(Caption("")))]
        pv_records = add_smiles_perovskite_htl(pv_records)
        self.assertEqual(pv_records[0].htl, expected)

    def test_smiles_perovskite_htl_from_compound(self):

        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'htl': {'HoleTransportLayer': {'raw_value': 'CuSCN', 'specifier': 'HTL',
                             'compound': {'names': ["Copper(I) thiocyanate"], 'labels': ['3c']}}}
        }

        expected = {'HoleTransportLayer': {'compound': {'labels': ['3c'],
                                     'names': ['Copper(I) thiocyanate']},
                        'raw_value': 'CuSCN',
                        'smiles': {'context': 'compound',
                                   'value': 'C(#N)[S-].[Cu+]'},
                        'specifier': 'HTL'}}

        pv_records = [PerovskiteRecord(input, Table(Caption("")))]
        pv_records = add_smiles_perovskite_htl(pv_records)
        self.assertEqual(pv_records[0].htl, expected)

    def test_smiles_perovskite_htl_from_raw_value(self):

        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'htl': {'HoleTransportLayer': {'raw_value': "Spiro-OMeTAD", 'specifier': 'HTL'}
                    }
        }

        expected = {'HoleTransportLayer': {'raw_value': 'Spiro-OMeTAD',
                        'smiles': {'context': 'raw_value',
                                   'value': 'COC1=CC=C(C=C1)N(C2=CC=C(C=C2)OC)C3=CC4=C(C=C3)C5=C(C46C7=C(C=CC(=C7)N(C8=CC=C(C=C8)OC)C9=CC=C(C=C9)OC)C1=C6C=C(C=C1)N(C1=CC=C(C=C1)OC)C1=CC=C(C=C1)OC)C=C(C=C5)N(C1=CC=C(C=C1)OC)C1=CC=C(C=C1)OC'},
                        'specifier': 'HTL'}}

        pv_records = [PerovskiteRecord(input, Table(Caption("")))]
        pv_records = add_smiles_perovskite_htl(pv_records)
        self.assertEqual(pv_records[0].htl, expected)