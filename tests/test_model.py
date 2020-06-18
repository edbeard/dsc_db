"""
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import unittest

from dsc_db.model import PhotovoltaicRecord, PerovskiteRecord
from pprint import pprint

from chemdataextractor import Document
from chemdataextractor.model import Compound
from chemdataextractor.model.pv_model import PhotovoltaicCell


class TestModel(unittest.TestCase):
    
    def test_model_initialized(self):
        """ Simple initialization test to ensure all omitted fields are set to none"""

        input = {'counter_electrode': {'CounterElectrode': {'raw_value': 'NiSe2 '
                                                                                      '- '
                                                                                      '180',
                                                                         'specifier': 'CE'}},
                              'ff': {'FillFactor': {'raw_value': '0.664',
                                                    'specifier': 'FF',
                                                    'value': [0.664]}},
                              'jsc': {'ShortCircuitCurrentDensity': {'raw_units': '(mAcm–2)',
                                                                     'raw_value': '15.49',
                                                                     'specifier': 'Jsc',
                                                                     'units': '(10^1.0) '
                                                                              '* '
                                                                              'Ampere^(1.0)  '
                                                                              'Meter^(-2.0)',
                                                                     'value': [15.49]}},
                              'pce': {'PowerConversionEfficiency': {'raw_units': '(%)',
                                                                    'raw_value': '7.78',
                                                                    'specifier': 'PCE',
                                                                    'units': 'Percent^(1.0)',
                                                                    'value': [7.78]}},
                              'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                             'raw_value': '756',
                                                             'specifier': 'Voc',
                                                             'units': '(10^-3.0) '
                                                                      '* '
                                                                      'Volt^(1.0)',
                                                             'value': [756.0]}}}



        input_doc = Document()
        expected = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'pce': {'PowerConversionEfficiency': {'raw_units': '(%)', 'raw_value': '7.78', 'specifier': 'PCE',
                                              'units': 'Percent^(1.0)', 'value': [7.78]}},
            'ff': {'FillFactor': {'raw_value': '0.664', 'specifier': 'FF', 'value': [0.664]}},
            'jsc': {'ShortCircuitCurrentDensity': {'raw_units': '(mAcm–2)',
                                                   'raw_value': '15.49',
                                                   'specifier': 'Jsc',
                                                   'units': '(10^1.0) '
                                                            '* '
                                                            'Ampere^(1.0)  '
                                                            'Meter^(-2.0)',
                                                   'value': [15.49]}},
            'dye': None,
            'ref': None,
            'isc': None,
            'pin': None,
            'pmax': None,
            'redox_couple': None,
            'dye_loading': None,
            'counter_electrode': {'CounterElectrode': {'raw_value': 'NiSe2 - 180', 'specifier': 'CE'}},
            'semiconductor': None,
            'active_area': None,
            'solar_simulator': None,
            'specific_charge_transfer_resistance': None,
            'specific_series_resistance': None,
            'electrolyte': None,
            'substrate': None,
            'charge_transfer_resistance': None,
            'series_resistance': None,
            'exposure_time': None,
            'table_row_categories': None,
            'derived_properties': None
        }

        record = PhotovoltaicRecord(input)
        result = record.serialize(include_none=True)
        pprint(record)
        self.assertEqual(result, expected)

    def test_model_initialized_resistance_property(self):

        input = {'charge_transfer_resistance': {'ChargeTransferResistance': {'raw_value': '6.75 ',
                                                                         'specifier': 'CE',
                                                                             'value': [6.75]}},
                              'ff': {'FillFactor': {'raw_value': '0.664',
                                                    'specifier': 'FF',
                                                    'value': [0.664]}},
                              'jsc': {'ShortCircuitCurrentDensity': {'raw_units': '(mAcm–2)',
                                                                     'raw_value': '15.49',
                                                                     'specifier': 'Jsc',
                                                                     'units': '(10^1.0) '
                                                                              '* '
                                                                              'Ampere^(1.0)  '
                                                                              'Meter^(-2.0)',
                                                                     'value': [15.49]}},
                              'pce': {'PowerConversionEfficiency': {'raw_units': '(%)',
                                                                    'raw_value': '7.78',
                                                                    'specifier': 'PCE',
                                                                    'units': 'Percent^(1.0)',
                                                                    'value': [7.78]}},
                              'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                             'raw_value': '756',
                                                             'specifier': 'Voc',
                                                             'units': '(10^-3.0) '
                                                                      '* '
                                                                      'Volt^(1.0)',
                                                             'value': [756.0]}}}

        expected = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'pce': {'PowerConversionEfficiency': {'raw_units': '(%)', 'raw_value': '7.78', 'specifier': 'PCE',
                                              'units': 'Percent^(1.0)', 'value': [7.78]}},
            'ff': {'FillFactor': {'raw_value': '0.664', 'specifier': 'FF', 'value': [0.664]}},
            'jsc': {'ShortCircuitCurrentDensity': {'raw_units': '(mAcm–2)',
                                                   'raw_value': '15.49',
                                                   'specifier': 'Jsc',
                                                   'units': '(10^1.0) '
                                                            '* '
                                                            'Ampere^(1.0)  '
                                                            'Meter^(-2.0)',
                                                   'value': [15.49]}},
            'dye': None,
            'ref': None,
            'isc': None,
            'pin': None,
            'pmax': None,
            'redox_couple': None,
            'dye_loading': None,
            'counter_electrode': None,
            'semiconductor': None,
            'active_area': None,
            'solar_simulator': None,
            'specific_charge_transfer_resistance': None,
            'specific_series_resistance': None,
            'electrolyte': None,
            'substrate': None,
            'charge_transfer_resistance': None,
            'series_resistance': None,
            'exposure_time': None,
            'table_row_categories': None,
            'derived_properties': None
        }

        record = PhotovoltaicRecord(input)
        result = record.serialize(include_none=True)
        pprint(record)
        self.assertEqual(result, expected)


    def test_substitute_abbreviations(self):
        input = {'counter_electrode': {'CounterElectrode': {'raw_value': 'Ni-Co-Se',
                                                    'specifier': 'CE'}}}
        doc = Document('Ternary nickel cobalt selenide (Ni-Co-Se) ')
        expected = {'counter_electrode': {'CounterElectrode': {'raw_value': 'Ni-Co-Se', 'specifier': 'CE', 'abbreviations': [['nickel', 'cobalt', 'selenide']]}}}

        pv_record = PhotovoltaicRecord(input, None)
        pv_record._substitute_definitions('counter_electrode', 'CounterElectrode', doc)
        self.assertEqual(pv_record.serialize(), expected)

    def test_substitute_compound_names(self):
        input = {'counter_electrode': {'CounterElectrode': {'raw_value': 'NiSe',
                                                    'specifier': 'CE'}}}
        expected = {'counter_electrode': {'CounterElectrode': {'raw_value': 'NiSe',
                                                    'specifier': 'CE', 'compound': {'names':['NiSe']}}}}

        doc = Document('NiSe.')
        doc.add_models([PhotovoltaicCell, Compound])

        doc_records = [record.serialize() for record in doc.records]
        compound_records = [record['Compound'] for record in doc_records if 'Compound' in record.keys()]

        pv_record = PhotovoltaicRecord(input, None)
        pv_record._substitute_compound('counter_electrode', 'CounterElectrode', compound_records)
        self.assertEqual(pv_record.serialize(), expected)

    def test_substitute_abbreviations_perov_htl(self):
        input = {'htl': {'HoleTransportLayer': {'raw_value': 'PTAA',
                                                    'specifier': 'HTL'}}}
        doc = Document('poly(triarylamine) (PTAA) ')
        expected = {'htl': {'HoleTransportLayer': {'abbreviations': [['poly(triarylamine)']],
                                'raw_value': 'PTAA',
                                'specifier': 'HTL'}}}

        pv_record = PerovskiteRecord(input, None)
        pv_record._substitute_definitions('htl', 'HoleTransportLayer', doc)
        self.assertEqual(pv_record.serialize(), expected)

    def test_substitute_compound_perov_htl(self):
        input = {'htl': {'HoleTransportLayer': {'raw_value': 'poly(triarylamine)',
                                                    'specifier': 'HTL'}}}
        expected = {'htl': {'HoleTransportLayer': {'compound': {'names': ['poly(triarylamine)']},
                                'raw_value': 'poly(triarylamine)',
                                'specifier': 'HTL'}}}

        doc = Document('poly(triarylamine).')
        doc.add_models([PhotovoltaicCell, Compound])

        doc_records = [record.serialize() for record in doc.records]
        compound_records = [record['Compound'] for record in doc_records if 'Compound' in record.keys()]

        pv_record = PerovskiteRecord(input, None)
        pv_record._substitute_compound('htl', 'HoleTransportLayer', compound_records)
        self.assertEqual(pv_record.serialize(), expected)

if __name__ == '__main__':
    unittest.main()
