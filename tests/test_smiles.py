"""
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import unittest

from chemdataextractor.doc import Table, Caption

from dsc_db.smiles import get_smiles_pubchem, add_smiles
from dsc_db.model import PhotovoltaicRecord


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
