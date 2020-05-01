"""
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import unittest

from dsc_db.model import PhotovoltaicRecord
from dsc_db.calculate import calculate_metrics, calculate_irradiance, calculate_relative_metrics
from dsc_db.run import get_table_records
from pprint import pprint

from chemdataextractor import Document
from chemdataextractor.model import Compound
from chemdataextractor.doc.table import Table
from chemdataextractor.doc.text import Caption
from chemdataextractor.model.pv_model import PhotovoltaicCell, OpenCircuitVoltage, ShortCircuitCurrentDensity, FillFactor, PowerConversionEfficiency
from chemdataextractor.model.units import Volt, Percent
from chemdataextractor.model.units.current_density import AmpPerMeterSquared


class TestCalculate(unittest.TestCase):

    def test_calculate_irradiance(self):

        voc = OpenCircuitVoltage(value=[756.0], units=Volt(magnitude=-3.))
        jsc = ShortCircuitCurrentDensity(value=[15.49], units=AmpPerMeterSquared(magnitude=1.))
        ff = FillFactor(value=[0.664])
        pce = PowerConversionEfficiency(value=[7.78], units=Percent())
        input_record = PhotovoltaicCell(voc=voc, jsc=jsc, ff=ff, pce=pce)
        output_record = calculate_irradiance(input_record)
        expected = 999.5
        irradiance = output_record.calculated_properties['solar_simulator'].value
        self.assertEqual(irradiance[0], expected)

    def test_calculate_irradiance_no_unit_jsc(self):
        voc = OpenCircuitVoltage(value=[756.0], units=Volt(magnitude=-3.))
        jsc = ShortCircuitCurrentDensity(value=[15.49])
        input_record2 = PhotovoltaicCell(voc=voc, jsc=jsc)
        output_record2 = calculate_irradiance(input_record2)
        self.assertFalse(output_record2.calculated_properties)

    def test_generate_inputs_for_calculating_metrics(self):
        table_input = [['CE',	'Jsc (mA cm−2)', 'Voc (V)', 'FF', 'PCE'], ['Pt', '11.11', '22.22', '33.33', '44.44'],
                       ['Novel electrode', '55.55', '66.66', '77.77', '88.88']]
        input_table = Table(caption=Caption(''), table_data=table_input)
        doc = Document('Null', input_table)
        doc.add_models([PhotovoltaicCell, Compound])
        records = get_table_records(doc, 'PhotovoltaicCell')

        for record in records:
            print(record[0])

    def test_classify_table_counter_electrode_2(self):

        records = [{'voc': {'OpenCircuitVoltage': {'raw_value': '22.22', 'raw_units': '(V)', 'value': [22.22],
                                                     'units': 'Volt^(1.0)', 'specifier': 'Voc', 'std_units': 'Volt^(1.0)', 'std_value': [22.22]}},
                      'ff': {'FillFactor': {'raw_value': '33.33', 'value': [33.33], 'specifier': 'FF'}},
                      'pce': {'PowerConversionEfficiency': {'raw_value': '44.44', 'value': [44.44], 'specifier': 'PCE'}},
                      'jsc': {'ShortCircuitCurrentDensity': {'raw_value': '11.11', 'raw_units': '(mAcm−2)', 'value': [11.11], 'units': '(10^1.0) * Ampere^(1.0)  Meter^(-2.0)',
                                                             'specifier': 'Jsc', 'std_units': 'Ampere^(1.0)  Meter^(-2.0)', 'std_value': [111.1]}},
                      'counter_electrode': {'CounterElectrode': {'specifier': 'CE', 'raw_value': 'Novel electrode'}},
                      'calculated_properties': {'solar_simulator': {'value': [1851.5], 'units': 'WattPerMeterSquared^(1.0)'}},
                      'table_row_categories': 'Pt'},

                      {'voc': {'OpenCircuitVoltage': {'raw_value': '66.66', 'raw_units': '(V)', 'value': [66.66],
                                                      'units': 'Volt^(1.0)', 'specifier': 'Voc', 'std_units': 'Volt^(1.0)',
                                                      'std_value': [66.66]}},
                       'ff': {'FillFactor': {'raw_value': '77.77', 'value': [77.77], 'specifier': 'FF'}},
                       'pce': {'PowerConversionEfficiency': {'raw_value': '88.88', 'value': [88.88], 'specifier': 'PCE'}},
                       'jsc': {'ShortCircuitCurrentDensity': {'raw_value': '55.55', 'raw_units': '(mAcm−2)',
                                                              'value': [55.55], 'units': '(10^1.0) * Ampere^(1.0)  Meter^(-2.0)',
                                                              'specifier': 'Jsc', 'std_units': 'Ampere^(1.0)  Meter^(-2.0)', 'std_value': [555.5]}},
                       'counter_electrode': {'CounterElectrode': {'specifier': 'CE', 'raw_value': ' Pt '}},
                       'calculated_properties': {'solar_simulator': {'value': [32400.9], 'units': 'WattPerMeterSquared^(1.0)'}},
                       'table_row_categories': 'Novel electrode'}]

        records = calculate_relative_metrics(records)
        self.assertEqual(records[0]['pce']['PowerConversionEfficiency']['normalized_value'], 0.5)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized_value'], 1.0)








