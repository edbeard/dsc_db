"""
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import unittest

from dsc_db.calculate import calculate_irradiance, calculate_relative_metrics, \
    calc_error_quantity, round_to_sig_figs, calculate_current_density, calculate_current, calculate_specific_resistance_rct, \
    calculate_specific_resistance_rs, calculate_resistance_rct, calculate_resistance_rs, calculate_metrics, calculate_power_in, \
    calculate_power_max, calculate_relative_metrics_perovskite
from dsc_db.run import get_table_records
from copy import deepcopy
from pprint import pprint

from chemdataextractor import Document
from chemdataextractor.model import Compound
from chemdataextractor.doc.table import Table
from chemdataextractor.doc.text import Caption
from chemdataextractor.model.pv_model import PhotovoltaicCell, OpenCircuitVoltage, ShortCircuitCurrentDensity, FillFactor,\
    PowerConversionEfficiency, ShortCircuitCurrent, SpecificChargeTransferResistance, SpecificSeriesResistance, \
    ChargeTransferResistance, SeriesResistance, SimulatedSolarLightIntensity, PowerIn, PowerMax
from chemdataextractor.model.units import Volt, Percent, Ampere
from chemdataextractor.model.units.area import MetersSquaredAreaUnit
from chemdataextractor.model.units.current_density import AmpPerMeterSquared
from chemdataextractor.model.units.irradiance import WattPerMeterSquared
from chemdataextractor.model.units.power import Watt
from chemdataextractor.model.units.resistance import Ohm

test_records_pt = [{'voc': {'OpenCircuitVoltage': {'raw_value': '22.22', 'raw_units': '(V)', 'value': [22.22],
                                                     'units': 'Volt^(1.0)', 'specifier': 'Voc', 'std_units': 'Volt^(1.0)', 'std_value': [22.22]}},
                      'ff': {'FillFactor': {'raw_value': '33.33', 'value': [33.33], 'specifier': 'FF'}},
                      'pce': {'PowerConversionEfficiency': {'raw_value': '44.44', 'value': [44.44], 'specifier': 'PCE'}},
                      'jsc': {'ShortCircuitCurrentDensity': {'raw_value': '11.11', 'raw_units': '(mAcm−2)', 'value': [11.11], 'units': '(10^1.0) * Ampere^(1.0)  Meter^(-2.0)',
                                                             'specifier': 'Jsc', 'std_units': 'Ampere^(1.0)  Meter^(-2.0)', 'std_value': [111.1]}},
                      'counter_electrode': {'CounterElectrode': {'specifier': 'CE', 'raw_value': 'Novel electrode'}},
                      'derived_properties': {'solar_simulator': {'value': [1851.5], 'units': 'WattPerMeterSquared^(1.0)'}},
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
                       'derived_properties': {'solar_simulator': {'value': [32400.9], 'units': 'WattPerMeterSquared^(1.0)'}},
                       'table_row_categories': 'Novel electrode'}]

test_records_n719 = [{'derived_properties': {'solar_simulator': {'units': 'WattPerMeterSquared^(1.0)',
                                                                       'value': [1851.5]}},
                         'dye': {'Dye': {'raw_value': 'N719', 'specifier': 'Dye'}},
                         'ff': {'FillFactor': {'raw_value': '33.33',
                                               'specifier': 'FF',
                                               'value': [33.33]}},
                         'jsc': {'ShortCircuitCurrentDensity': {'raw_units': '(mAcm−2)',
                                                                'raw_value': '11.11',
                                                                'specifier': 'Jsc',
                                                                'std_units': 'Ampere^(1.0)  '
                                                                             'Meter^(-2.0)',
                                                                'std_value': [111.1],
                                                                'units': '(10^1.0) * Ampere^(1.0)  '
                                                                         'Meter^(-2.0)',
                                                                'value': [11.11]}},
                         'pce': {'PowerConversionEfficiency': {'raw_value': '88.88',
                                                               'specifier': 'PCE',
                                                               'value': [88.88]}},
                         'table_row_categories': 'N719',
                         'voc': {'OpenCircuitVoltage': {'raw_units': '(V)',
                                                        'raw_value': '22.22',
                                                        'specifier': 'Voc',
                                                        'std_units': 'Volt^(1.0)',
                                                        'std_value': [22.22],
                                                        'units': 'Volt^(1.0)',
                                                        'value': [22.22]}}},
                        {'derived_properties': {'solar_simulator': {'units': 'WattPerMeterSquared^(1.0)',
                                                                       'value': [32400.9]}},
                         'dye': {'Dye': {'raw_value': 'Novel dye', 'specifier': 'Dye'}},
                         'ff': {'FillFactor': {'raw_value': '77.77',
                                               'specifier': 'FF',
                                               'value': [77.77]}},
                         'jsc': {'ShortCircuitCurrentDensity': {'raw_units': '(mAcm−2)',
                                                                'raw_value': '55.55',
                                                                'specifier': 'Jsc',
                                                                'std_units': 'Ampere^(1.0)  '
                                                                             'Meter^(-2.0)',
                                                                'std_value': [555.5],
                                                                'units': '(10^1.0) * Ampere^(1.0)  '
                                                                         'Meter^(-2.0)',
                                                                'value': [55.55]}},
                         'pce': {'PowerConversionEfficiency': {'raw_value': '44.44',
                                                               'specifier': 'PCE',
                                                               'value': [44.44]}},
                         'table_row_categories': 'Novel dye',
                         'voc': {'OpenCircuitVoltage': {'raw_units': '(V)',
                                                        'raw_value': '66.66',
                                                        'specifier': 'Voc',
                                                        'std_units': 'Volt^(1.0)',
                                                        'std_value': [66.66],
                                                        'units': 'Volt^(1.0)',
                                                        'value': [66.66]}}}]

test_records_tio2 = [{'derived_properties': {'solar_simulator': {'units': 'WattPerMeterSquared^(1.0)',
                                               'value': [1851.5]}},
                         'ff': {'FillFactor': {'raw_value': '33.33',
                                               'specifier': 'FF',
                                               'value': [33.33]}},
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
                         'semiconductor': {'Semiconductor': {'raw_value': 'Novel SC',
                                                             'specifier': 'Semiconductor'}},
                         'table_row_categories': 'Novel SC',
                         'voc': {'OpenCircuitVoltage': {'raw_units': '(V)',
                                                        'raw_value': '22.22',
                                                        'specifier': 'Voc',
                                                        'std_units': 'Volt^(1.0)',
                                                        'std_value': [22.22],
                                                        'units': 'Volt^(1.0)',
                                                        'value': [22.22]}}},
                        {'derived_properties': {'solar_simulator': {'units': 'WattPerMeterSquared^(1.0)',
                                                                       'value': [32400.9]}},
                         'ff': {'FillFactor': {'raw_value': '77.77',
                                               'specifier': 'FF',
                                               'value': [77.77]}},
                         'jsc': {'ShortCircuitCurrentDensity': {'raw_units': '(mAcm−2)',
                                                                'raw_value': '55.55',
                                                                'specifier': 'Jsc',
                                                                'std_units': 'Ampere^(1.0)  '
                                                                             'Meter^(-2.0)',
                                                                'std_value': [555.5],
                                                                'units': '(10^1.0) * Ampere^(1.0)  '
                                                                         'Meter^(-2.0)',
                                                                'value': [55.55]}},
                         'pce': {'PowerConversionEfficiency': {'raw_value': '88.88',
                                                               'specifier': 'PCE',
                                                               'value': [88.88]}},
                         'semiconductor': {'Semiconductor': {'raw_value': 'TiO2',
                                                             'specifier': 'Semiconductor'}},
                         'table_row_categories': ' TiO2',
                         'voc': {'OpenCircuitVoltage': {'raw_units': '(V)',
                                                        'raw_value': '66.66',
                                                        'specifier': 'Voc',
                                                        'std_units': 'Volt^(1.0)',
                                                        'std_value': [66.66],
                                                        'units': 'Volt^(1.0)',
                                                        'value': [66.66]}}}
                        ]

test_records_perovskite = [{'derived_properties': {'solar_simulator': {'units': 'WattPerMeterSquared^(1.0)',
                                               'value': [1851.5]}},
                         'ff': {'FillFactor': {'raw_value': '33.33',
                                               'specifier': 'FF',
                                               'value': [33.33]}},
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
                         'perovskite': {'Perovskite': {'raw_value': 'Novel sensitizer',
                                                             'specifier': 'perovskite'}},
                         'table_row_categories': 'Novel sensitizer',
                         'voc': {'OpenCircuitVoltage': {'raw_units': '(V)',
                                                        'raw_value': '22.22',
                                                        'specifier': 'Voc',
                                                        'std_units': 'Volt^(1.0)',
                                                        'std_value': [22.22],
                                                        'units': 'Volt^(1.0)',
                                                        'value': [22.22]}}},
                           {'derived_properties': {'solar_simulator': {'units': 'WattPerMeterSquared^(1.0)',
                                                                          'value': [32400.9]}},
                            'ff': {'FillFactor': {'raw_value': '77.77',
                                                  'specifier': 'FF',
                                                  'value': [77.77]}},
                            'jsc': {'ShortCircuitCurrentDensity': {'raw_units': '(mAcm−2)',
                                                                   'raw_value': '55.55',
                                                                   'specifier': 'Jsc',
                                                                   'std_units': 'Ampere^(1.0)  '
                                                                                'Meter^(-2.0)',
                                                                   'std_value': [555.5],
                                                                   'units': '(10^1.0) * Ampere^(1.0)  '
                                                                            'Meter^(-2.0)',
                                                                   'value': [55.55]}},
                            'pce': {'PowerConversionEfficiency': {'raw_value': '88.88',
                                                                  'specifier': 'PCE',
                                                                  'value': [88.88]}},
                            'perovskite': {'Perovskite': {'raw_value': 'CH3NH3PbI3',
                                                          'specifier': 'perovskite'}},
                            'table_row_categories': ' CH3NH3PbI3',
                            'voc': {'OpenCircuitVoltage': {'raw_units': '(V)',
                                                           'raw_value': '66.66',
                                                           'specifier': 'Voc',
                                                           'std_units': 'Volt^(1.0)',
                                                           'std_value': [66.66],
                                                           'units': 'Volt^(1.0)',
                                                           'value': [66.66]}}}
                           ]


class TestCalculate(unittest.TestCase):

    def test_calculate_irradiance(self):

        voc = OpenCircuitVoltage(value=[756.0], units=Volt(magnitude=-3.), raw_value='756.0')
        jsc = ShortCircuitCurrentDensity(value=[15.49], units=AmpPerMeterSquared(magnitude=1.), raw_value='15.49')
        ff = FillFactor(value=[0.664], raw_value='0.664')
        pce = PowerConversionEfficiency(value=[7.78], units=Percent(), raw_value='7.78')
        input_record = PhotovoltaicCell(voc=voc, jsc=jsc, ff=ff, pce=pce)
        output_record = calculate_irradiance(input_record)
        expected = 999.0
        irradiance = output_record.derived_properties['solar_simulator'].value
        self.assertEqual(irradiance[0], expected)

    def test_calculate_irradiance_no_unit_jsc(self):
        voc = OpenCircuitVoltage(value=[756.0], units=Volt(magnitude=-3.))
        jsc = ShortCircuitCurrentDensity(value=[15.49])
        input_record2 = PhotovoltaicCell(voc=voc, jsc=jsc)
        output_record2 = calculate_irradiance(input_record2)
        self.assertFalse(output_record2.derived_properties)

    def test_calculate_irradaince_ff_with_unit(self):
        voc = OpenCircuitVoltage(value=[756.0], units=Volt(magnitude=-3.), raw_value='756.0')
        jsc = ShortCircuitCurrentDensity(value=[15.49], units=AmpPerMeterSquared(magnitude=1.), raw_value='15.49')
        ff = FillFactor(value=[0.2], raw_value='0.2', units=Percent(), raw_units='(%)')
        pce = PowerConversionEfficiency(value=[7.78], units=Percent(), raw_value='7.78', raw_units='(%)')
        input_record = PhotovoltaicCell(voc=voc, jsc=jsc, ff=ff, pce=pce)
        output_record = calculate_irradiance(input_record)
        expected = 3.0
        irradiance = output_record.derived_properties['solar_simulator'].value
        self.assertEqual(irradiance[0], expected)

    def test_calculate_irradiance_ff_too_large(self):
        voc = OpenCircuitVoltage(value=[756.0], units=Volt(magnitude=-3.), raw_value='756.0')
        jsc = ShortCircuitCurrentDensity(value=[15.49], units=AmpPerMeterSquared(magnitude=1.), raw_value='15.49')
        ff = FillFactor(value=[0.48], raw_value='0.48')
        pce = PowerConversionEfficiency(value=[7.78], units=Percent(), raw_value='7.78')
        input_record = PhotovoltaicCell(voc=voc, jsc=jsc, ff=ff, pce=pce)
        output_record = calculate_irradiance(input_record)
        expected = 720
        irradiance = output_record.derived_properties['solar_simulator'].value
        self.assertEqual(irradiance[0], expected)

    def test_calculate_irradiance_only_isc(self):
        """
        Testing that the value of jsc derived from isc is used in the absence of an extracted jsc value
        """

        voc = OpenCircuitVoltage(value=[756.0], units=Volt(magnitude=-3.), raw_value='756.0')
        isc = ShortCircuitCurrent(value=[0.653], units=Ampere(magnitude=-3), raw_value='0.653')
        ff = FillFactor(value=[0.48], raw_value='0.48')
        pce = PowerConversionEfficiency(value=[7.78], units=Percent(), raw_value='7.78')
        input_record = PhotovoltaicCell(voc=voc, isc=isc, ff=ff, pce=pce)

        active_area_record = {'ActiveArea': {'contextual': 'document',
                'raw_units': 'cm2',
                'raw_value': '0.26',
                'specifier': 'active area',
                'std_units': 'Meter^(2.0)',
                'std_value': [2.6000000000000005e-05],
                'units': '(10^-4.0) * Meter^(2.0)',
                'value': [0.26]}}

        output_record = calculate_metrics(input_record, active_area_record)
        expected = 117.
        irradiance = output_record.derived_properties['solar_simulator'].value
        self.assertEqual(irradiance[0], expected)


    def test_calculate_jsc(self):
        isc = ShortCircuitCurrent(value=[0.653], units=Ampere(magnitude=-3), raw_value='0.653')
        active_area_record = {'ActiveArea': {'contextual': 'document',
                'raw_units': 'cm2',
                'raw_value': '0.26',
                'specifier': 'active area',
                'std_units': 'Meter^(2.0)',
                'std_value': [2.6000000000000005e-05],
                'units': '(10^-4.0) * Meter^(2.0)',
                'value': [0.26]}}
        input_record = PhotovoltaicCell(isc=isc)
        output_record = calculate_current_density(input_record, active_area_record)
        jsc = output_record.derived_properties['jsc'].value
        expected = 25.0
        self.assertEqual(jsc[0], expected)

    def test_calculate_isc(self):
        jsc = ShortCircuitCurrentDensity(value=[15.49], units=AmpPerMeterSquared(magnitude=1.), raw_value='15.49')
        active_area_record = {'ActiveArea': {'contextual': 'document',
                'raw_units': 'cm2',
                'raw_value': '0.26',
                'specifier': 'active area',
                'std_units': 'Meter^(2.0)',
                'std_value': [2.6000000000000005e-05],
                'units': '(10^-4.0) * Meter^(2.0)',
                'value': [0.26]}}
        input_record = PhotovoltaicCell(jsc=jsc)
        output_record = calculate_current(input_record, active_area_record)
        isc = output_record.derived_properties['isc'].value
        isc_error = output_record.derived_properties['isc'].error
        expected_val = 0.0040
        expected_err = 0.0002
        self.assertEqual(isc[0], expected_val)
        self.assertEqual(isc_error, expected_err)

    def test_calculate_sp_rct(self):
        rct = ChargeTransferResistance(value=[15.49], units=Ohm(), raw_value='15.49')
        active_area_record = {'ActiveArea': {'contextual': 'document',
                'raw_units': 'cm2',
                'raw_value': '0.26',
                'specifier': 'active area',
                'std_units': 'Meter^(2.0)',
                'std_value': [2.6000000000000005e-05],
                'units': '(10^-4.0) * Meter^(2.0)',
                'value': [0.26]}}
        input_record = PhotovoltaicCell(charge_transfer_resistance=rct)
        output_record = calculate_specific_resistance_rct(input_record, active_area_record)
        sp_rct = output_record.derived_properties['specific_charge_transfer_resistance'].value
        sp_rct_error = output_record.derived_properties['specific_charge_transfer_resistance'].error
        expected_val = 0.00040
        expected_err = 0.00002
        self.assertEqual(sp_rct[0], expected_val)
        self.assertEqual(sp_rct_error, expected_err)

    def test_calculate_sp_rs(self):
        rs = SeriesResistance(value=[7.89], units=Ohm(), raw_value='7.89')
        active_area_record = {'ActiveArea': {'contextual': 'document',
                'raw_units': 'cm2',
                'raw_value': '0.26',
                'specifier': 'active area',
                'std_units': 'Meter^(2.0)',
                'std_value': [2.6000000000000005e-05],
                'units': '(10^-4.0) * Meter^(2.0)',
                'value': [0.26]}}
        input_record = PhotovoltaicCell(series_resistance=rs)
        output_record = calculate_specific_resistance_rs(input_record, active_area_record)
        sp_rs = output_record.derived_properties['specific_series_resistance'].value
        sp_rs_error = output_record.derived_properties['specific_series_resistance'].error
        expected_val = 0.000205
        expected_err = 0.000008
        self.assertEqual(sp_rs[0], expected_val)
        self.assertEqual(sp_rs_error, expected_err)

    def test_calculate_rct(self):
        sp_rct = SpecificChargeTransferResistance(value=[5.3], units=(Ohm() * MetersSquaredAreaUnit(magnitude=-4)), raw_value='5.3')
        active_area_record = {'ActiveArea': {'contextual': 'document',
                'raw_units': 'cm2',
                'raw_value': '0.26',
                'specifier': 'active area',
                'std_units': 'Meter^(2.0)',
                'std_value': [2.6000000000000005e-05],
                'units': '(10^-4.0) * Meter^(2.0)',
                'value': [0.26]}}
        input_record = PhotovoltaicCell(specific_charge_transfer_resistance=sp_rct)
        output_record = calculate_resistance_rct(input_record, active_area_record)
        rct = output_record.derived_properties['charge_transfer_resistance'].value
        rct_error = output_record.derived_properties['charge_transfer_resistance'].error
        expected_val = 20.4
        expected_err = 0.9
        self.assertEqual(rct[0], expected_val)
        self.assertEqual(rct_error, expected_err)

    def test_calculate_rs(self):
        sp_rs = SpecificSeriesResistance(value=[7.89], units=(Ohm() * MetersSquaredAreaUnit(magnitude=-4)), raw_value='7.89')
        active_area_record = {'ActiveArea': {'contextual': 'document',
                'raw_units': 'cm2',
                'raw_value': '0.26',
                'specifier': 'active area',
                'std_units': 'Meter^(2.0)',
                'std_value': [2.6000000000000005e-05],
                'units': '(10^-4.0) * Meter^(2.0)',
                'value': [0.26]}}
        input_record = PhotovoltaicCell(specific_series_resistance=sp_rs)
        output_record = calculate_resistance_rs(input_record, active_area_record)
        rs = output_record.derived_properties['series_resistance'].value
        rs_error = output_record.derived_properties['series_resistance'].error
        expected_val = 30.0
        expected_err = 1
        self.assertEqual(rs[0], expected_val)
        self.assertEqual(rs_error, expected_err)

    def test_calculate_pin_extracted_from_document(self):
        solar_simulator = SimulatedSolarLightIntensity(value=[1000], units=WattPerMeterSquared(), raw_value='1000')
        active_area_record = {'ActiveArea': {'contextual': 'document',
                'raw_units': 'cm2',
                'raw_value': '0.26',
                'specifier': 'active area',
                'std_units': 'Meter^(2.0)',
                'std_value': [2.6000000000000005e-05],
                'units': '(10^-4.0) * Meter^(2.0)',
                'value': [0.26]}}
        input_record = PhotovoltaicCell(solar_simulator=solar_simulator)
        output_record = calculate_power_in(input_record, active_area_record)
        pin = output_record.derived_properties['pin'].value
        pin_error = output_record.derived_properties['pin'].error
        expected_val = 0.026
        expected_err = 0.001
        self.assertEqual(pin[0], expected_val)
        self.assertEqual(pin_error, expected_err)

    def test_calculate_pin_derived_solar_simulator(self):
        """
        Testing that the value of jsc derived from isc is used in the absence of an extracted jsc value
        """

        voc = OpenCircuitVoltage(value=[756.0], units=Volt(magnitude=-3.), raw_value='756.0')
        jsc = ShortCircuitCurrentDensity(value=[15.49], units=AmpPerMeterSquared(magnitude=1.), raw_value='15.49')
        ff = FillFactor(value=[0.48], raw_value='0.48')
        pce = PowerConversionEfficiency(value=[7.78], units=Percent(), raw_value='7.78')
        input_record = PhotovoltaicCell(voc=voc, jsc=jsc, ff=ff, pce=pce)

        active_area_record = {'ActiveArea': {'contextual': 'document',
                'raw_units': 'cm2',
                'raw_value': '0.26',
                'specifier': 'active area',
                'std_units': 'Meter^(2.0)',
                'std_value': [2.6000000000000005e-05],
                'units': '(10^-4.0) * Meter^(2.0)',
                'value': [0.26]}}

        output_record = calculate_metrics(input_record, active_area_record)
        expected = 0.0187
        pin = output_record.derived_properties['pin'].value
        self.assertEqual(pin[0], expected)

    def test_calculate_pmax_extracted_from_document(self):

        pin = PowerIn(value=[100], units=Watt(magnitude=1.), raw_value='100')
        pce = PowerConversionEfficiency(value=[7.78], units=Percent(), raw_value='7.78')

        input_record = PhotovoltaicCell(pin=pin, pce=pce)
        output_record = calculate_power_max(input_record)
        pmax = output_record.derived_properties['pmax'].value
        pmax_error = output_record.derived_properties['pmax'].error
        expected_val = 77.8
        expected_err = 0.8
        self.assertEqual(pmax[0], expected_val)
        self.assertEqual(pmax_error, expected_err)

    def test_calculate_pmax_derived_pin(self):

        solar_simulator = SimulatedSolarLightIntensity(value=[1000], units=WattPerMeterSquared(), raw_value='1000')
        active_area_record = {'ActiveArea': {'contextual': 'document',
                'raw_units': 'cm2',
                'raw_value': '0.26',
                'specifier': 'active area',
                'std_units': 'Meter^(2.0)',
                'std_value': [2.6000000000000005e-05],
                'units': '(10^-4.0) * Meter^(2.0)',
                'value': [0.26]}}

        pce = PowerConversionEfficiency(value=[7.78], units=Percent(), raw_value='7.78')
        input_record = PhotovoltaicCell(pce=pce, solar_simulator=solar_simulator)
        output_record = calculate_metrics(input_record, active_area_record)
        pmax = output_record.derived_properties['pmax'].value
        pmax_error = output_record.derived_properties['pmax'].error
        expected_val = 0.00202
        expected_err = 8e-05
        self.assertEqual(pmax[0], expected_val)
        self.assertEqual(pmax_error, expected_err)

    def test_generate_inputs_for_calculating_metrics(self):
        table_input = [['Semiconductor', 'Jsc (mA cm−2)', 'Voc (V)', 'FF', 'PCE'], ['Novel SC', '11.11', '22.22', '33.33', '44.44'],
                       [' TiO2', '55.55', '66.66', '77.77', '88.88']]
        input_table = Table(caption=Caption(''), table_data=table_input)
        doc = Document('Null', input_table)
        doc.add_models([PhotovoltaicCell, Compound])
        records = get_table_records(doc, 'PhotovoltaicCell')

        for record in records:
            pprint(record[0])

    def test_classify_table_counter_electrode(self):

        records = deepcopy(test_records_pt)

        records = calculate_relative_metrics(records)
        self.assertEqual(records[0]['pce']['PowerConversionEfficiency']['normalized']['value'], 0.5)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['value'], 1.0)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['component_name'], 'counter_electrode')
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['std_component'], 'Pt')

    def test_classify_table_counter_electrode_one_without_ce_field(self):

        test_records = deepcopy(test_records_pt)
        altered_record = test_records[0]
        del(altered_record['counter_electrode'])
        records = [altered_record, test_records[1]]

        records = calculate_relative_metrics(records)
        self.assertTrue('normalized' not in records[1]['pce']['PowerConversionEfficiency'].keys())

    def test_classify_table_counter_electrode_has_no_name(self):

        test_records = deepcopy(test_records_pt)
        altered_record = test_records[0]
        del(altered_record['counter_electrode']['CounterElectrode']['raw_value'])
        records = [altered_record, test_records[1]]

        records = calculate_relative_metrics(records)
        self.assertTrue('normalized' not in records[1]['pce']['PowerConversionEfficiency'].keys())

    def test_classify_table_counter_electrode_has_no_platinum_record(self):

        test_records = deepcopy(test_records_pt)
        altered_record = test_records[1]
        altered_record['counter_electrode']['CounterElectrode']['raw_value'] = 'Not platinum'
        records = [test_records[0], altered_record]

        records = calculate_relative_metrics(records)
        self.assertTrue('normalized' not in records[1]['pce']['PowerConversionEfficiency'].keys())

    def test_classify_table_dye_N719(self):

        test_records = deepcopy(test_records_n719)
        records = calculate_relative_metrics(test_records)
        self.assertEqual(records[0]['pce']['PowerConversionEfficiency']['normalized']['value'], 1.0)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['value'], 0.5)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['component_name'], 'dye')
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['std_component'], 'N719')

    def test_classify_table_dye_N3(self):
        test_records = deepcopy(test_records_n719)
        test_records[0]['dye']['Dye']['raw_value'] = 'N3'
        records = calculate_relative_metrics(test_records)
        self.assertEqual(records[0]['pce']['PowerConversionEfficiency']['normalized']['value'], 1.0)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['value'], 0.5)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['component_name'], 'dye')
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['std_component'], 'N3')

    def test_classify_table_dye_one_without_dye_field(self):

        test_records = deepcopy(test_records_n719)
        altered_record = test_records[0]
        del(altered_record['dye'])
        records = [altered_record, test_records[1]]

        records = calculate_relative_metrics(records)
        self.assertTrue('normalized' not in records[1]['pce']['PowerConversionEfficiency'].keys())

    def test_classify_table_dye_has_no_name(self):

        test_records = deepcopy(test_records_n719)
        altered_record = test_records[0]
        del(altered_record['dye']['Dye']['raw_value'])
        records = [altered_record, test_records[1]]

        records = calculate_relative_metrics(records)
        self.assertTrue('normalized' not in records[1]['pce']['PowerConversionEfficiency'].keys())

    def test_classify_table_dye_has_no_n719_record(self):

        test_records = deepcopy(test_records_n719)
        altered_record = test_records[0]
        altered_record['dye']['Dye']['raw_value'] = 'Not platinum'
        records = [ altered_record, test_records[1]]

        records = calculate_relative_metrics(records)
        self.assertTrue('normalized' not in records[1]['pce']['PowerConversionEfficiency'].keys())

    def test_classify_table_semiconductor(self):

        test_records = deepcopy(test_records_tio2)
        records = calculate_relative_metrics(test_records)
        self.assertEqual(records[0]['pce']['PowerConversionEfficiency']['normalized']['value'], 0.5)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['value'], 1.0)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['component_name'], 'semiconductor')
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['std_component'], 'TiO2')

    def test_classify_perovskite_table(self):
        test_records = deepcopy(test_records_perovskite)
        records = calculate_relative_metrics_perovskite(test_records)
        self.assertEqual(records[0]['pce']['PowerConversionEfficiency']['normalized']['value'], 0.5)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['value'], 1.0)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['component_name'], 'perovskite')
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['std_component'], 'CH3NH3PbI3')

    def test_classify_htl_table(self):
        test_records = deepcopy(test_records_perovskite)
        test_records[0]['htl'] = {'HoleTransportLayer':{'raw_value': 'novel_htl'}}
        test_records[1]['htl'] = {'HoleTransportLayer':{'raw_value': 'Spiro-OMeTAD'}}
        test_records[0]['perovskite'] = {'Perovskite': {'raw_value': 'CH3NH3PbI3', 'specifier': 'perovskite'}}
        records = calculate_relative_metrics_perovskite(test_records)
        self.assertEqual(records[0]['pce']['PowerConversionEfficiency']['normalized']['value'], 0.5)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['value'], 1.0)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['component_name'], 'htl')
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['std_component'], 'Spiro-OMeTAD')

    def test_classify_htl_table_2(self):
        test_records = deepcopy(test_records_perovskite)
        test_records[0]['htl'] = {'HoleTransportLayer':{'raw_value': 'novel_htl'}}
        test_records[1]['htl'] = {'HoleTransportLayer':{'raw_value': 'PEDOT:PSS'}}
        test_records[0]['perovskite'] = {'Perovskite': {'raw_value': 'CH3NH3PbI3', 'specifier': 'perovskite'}}
        records = calculate_relative_metrics_perovskite(test_records)
        self.assertEqual(records[0]['pce']['PowerConversionEfficiency']['normalized']['value'], 0.5)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['value'], 1.0)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['component_name'], 'htl')
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['std_component'], 'PEDOT:PSS')

    def test_classify_htl_table_3(self):
        test_records = deepcopy(test_records_perovskite)
        test_records[0]['htl'] = {'HoleTransportLayer': {'raw_value': 'novel_htl'}}
        test_records[1]['htl'] = {'HoleTransportLayer': {'raw_value': 'PTAA'}}
        test_records[0]['perovskite'] = {'Perovskite': {'raw_value': 'CH3NH3PbI3', 'specifier': 'perovskite'}}
        records = calculate_relative_metrics_perovskite(test_records)
        self.assertEqual(records[0]['pce']['PowerConversionEfficiency']['normalized']['value'], 0.5)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['value'], 1.0)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['component_name'], 'htl')
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['std_component'], 'PTAA')

    def test_classify_etl_table(self):
        test_records = deepcopy(test_records_perovskite)
        test_records[0]['etl'] = {'ElectronTransportLayer':{'raw_value': 'novel_etl'}}
        test_records[1]['etl'] = {'ElectronTransportLayer':{'raw_value': 'TiO2'}}
        test_records[0]['perovskite'] = {'Perovskite': {'raw_value': 'CH3NH3PbI3', 'specifier': 'perovskite'}}
        records = calculate_relative_metrics_perovskite(test_records)
        self.assertEqual(records[0]['pce']['PowerConversionEfficiency']['normalized']['value'], 0.5)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['value'], 1.0)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['component_name'], 'etl')
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['std_component'], 'TiO2')

    def test_classify_etl_table_2(self):
        test_records = deepcopy(test_records_perovskite)
        test_records[0]['etl'] = {'ElectronTransportLayer':{'raw_value': 'novel_etl'}}
        test_records[1]['etl'] = {'ElectronTransportLayer':{'raw_value': 'ZnO'}}
        test_records[0]['perovskite'] = {'Perovskite': {'raw_value': 'CH3NH3PbI3', 'specifier': 'perovskite'}}
        records = calculate_relative_metrics_perovskite(test_records)
        self.assertEqual(records[0]['pce']['PowerConversionEfficiency']['normalized']['value'], 0.5)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['value'], 1.0)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['component_name'], 'etl')
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['std_component'], 'ZnO')

    def test_classify_counter_electrode_table_1(self):
        test_records = deepcopy(test_records_perovskite)
        test_records[0]['counter_electrode'] = {'CounterElectrode':{'raw_value': 'novel_electrode'}}
        test_records[1]['counter_electrode'] = {'CounterElectrode':{'raw_value': 'Ag'}}
        test_records[0]['perovskite'] = {'Perovskite': {'raw_value': 'CH3NH3PbI3', 'specifier': 'perovskite'}}
        records = calculate_relative_metrics_perovskite(test_records)
        self.assertEqual(records[0]['pce']['PowerConversionEfficiency']['normalized']['value'], 0.5)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['value'], 1.0)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['component_name'], 'counter_electrode')
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['std_component'], 'Ag')

    def test_classify_counter_electrode_table_2(self):
        test_records = deepcopy(test_records_perovskite)
        test_records[0]['counter_electrode'] = {'CounterElectrode':{'raw_value': 'novel_electrode'}}
        test_records[1]['counter_electrode'] = {'CounterElectrode':{'raw_value': 'Au'}}
        test_records[0]['perovskite'] = {'Perovskite': {'raw_value': 'CH3NH3PbI3', 'specifier': 'perovskite'}}
        records = calculate_relative_metrics_perovskite(test_records)
        self.assertEqual(records[0]['pce']['PowerConversionEfficiency']['normalized']['value'], 0.5)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['value'], 1.0)
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['component_name'], 'counter_electrode')
        self.assertEqual(records[1]['pce']['PowerConversionEfficiency']['normalized']['std_component'], 'Au')

    def test_calc_quantity_error_from_sig_figs(self):

        voc = OpenCircuitVoltage(value=[756.0], units=Volt(magnitude=-3.), raw_value='756.0')
        jsc = ShortCircuitCurrentDensity(value=[15.49], units=AmpPerMeterSquared(magnitude=1.), raw_value='15.49')
        ff = FillFactor(value=[0.664], raw_value='0.664')
        pce = PowerConversionEfficiency(value=[7.78], units=Percent(), raw_value='7.78')
        record = PhotovoltaicCell(voc=voc, jsc=jsc, ff=ff, pce=pce)

        derived_error1 = calc_error_quantity(record, 'voc')
        self.assertEqual(derived_error1, 0.0001)
        derived_error2 = calc_error_quantity(record, 'jsc')
        self.assertEqual(derived_error2, 0.1)
        derived_error3 = calc_error_quantity(record, 'ff')
        self.assertEqual(derived_error3, 0.001)
        derived_error4 = calc_error_quantity(record, 'pce')
        self.assertEqual(derived_error4, 0.0001)

    def test_calc_quantity_error_from_sig_figs_ranged_quantity(self):

        voc = OpenCircuitVoltage(value=[756, 759], units=Volt(magnitude=-3.), raw_value='756-759')
        jsc = ShortCircuitCurrentDensity(value=[15.5, 16.04], units=AmpPerMeterSquared(magnitude=1.), raw_value='15.5—16.04')
        record = PhotovoltaicCell(voc=voc, jsc=jsc)

        derived_error1 = calc_error_quantity(record, 'voc')
        self.assertEqual(derived_error1, 0.001)
        derived_error2 = calc_error_quantity(record, 'jsc')
        self.assertEqual(derived_error2, 1)

    def test_calc_quantity_error_from_sig_figs_negative_quantity(self):
        voc = OpenCircuitVoltage(value=[-756.0], units=Volt(magnitude=-3.), raw_value='-756.0')
        jsc = ShortCircuitCurrentDensity(value=[-15.5, -16.04], units=AmpPerMeterSquared(magnitude=1.), raw_value='-15.5—-16.04')

        record = PhotovoltaicCell(voc=voc, jsc=jsc)

        derived_error1 = calc_error_quantity(record, 'voc')
        self.assertEqual(derived_error1, 0.0001)
        derived_error2 = calc_error_quantity(record, 'jsc')
        self.assertEqual(derived_error2, 1)

    def test_calc_irradiance_error(self):

        voc = OpenCircuitVoltage(value=[756.0], units=Volt(magnitude=-3.), raw_value='756.0')
        jsc = ShortCircuitCurrentDensity(value=[15.49], units=AmpPerMeterSquared(magnitude=1.), raw_value='15.49')
        ff = FillFactor(value=[0.664], raw_value='0.664')
        pce = PowerConversionEfficiency(value=[7.78], units=Percent(), raw_value='7.78')
        record = PhotovoltaicCell(voc=voc, jsc=jsc, ff=ff, pce=pce)

        updated_record = calculate_irradiance(record)
        output = updated_record.derived_properties['solar_simulator']
        self.assertEqual(output.value, [999.0])
        self.assertEqual(output.error, 2.0)

    def test_explict_error_in_calculations(self):
        voc = OpenCircuitVoltage(value=[756.0], units=Volt(magnitude=-3.), raw_value='756.0', error=5.)
        jsc = ShortCircuitCurrentDensity(value=[15.49], units=AmpPerMeterSquared(magnitude=1.), raw_value='15.49', error= 1)
        ff = FillFactor(value=[0.664], raw_value='0.664')
        pce = PowerConversionEfficiency(value=[7.78], units=Percent(), raw_value='7.78')
        record = PhotovoltaicCell(voc=voc, jsc=jsc, ff=ff, pce=pce)

        updated_record = calculate_irradiance(record)
        output = updated_record.derived_properties['solar_simulator']
        self.assertEqual(output.value, [1000.0])
        self.assertEqual(output.error, 60.0)
        # self.assertEqual(irradiance[0], expected)

    def test_round_to_sig_figs(self):

        irr1, err1, exp1 = 999.45, 1, 999
        irr2, err2, exp2 = 986.31, 60, 990.
        irr3, err3, exp3 = 999.45, 0.1, 999.5
        irr4, err4, exp4 = 999.451234567, 0.00000001, 999.45123457
        irr5, err5, exp5 = 999.45123, 0.01, 999.45
        irr6, err6, exp6 = 123456.78, 3000, 123000.
        irr7, err7, exp7 = 0.002601, 0.00003, 0.00260
        irr8, err8, exp8 = 99999999999.9999999999, 0.000000001, 100000000000.

        self.assertEqual(round_to_sig_figs(irr1, err1), exp1)
        self.assertEqual(round_to_sig_figs(irr2, err2), exp2)
        self.assertEqual(round_to_sig_figs(irr3, err3), exp3)
        self.assertEqual(round_to_sig_figs(irr4, err4), exp4)
        self.assertEqual(round_to_sig_figs(irr5, err5), exp5)
        self.assertEqual(round_to_sig_figs(irr6, err6), exp6)
        self.assertEqual(round_to_sig_figs(irr7, err7), exp7)
        self.assertEqual(round_to_sig_figs(irr8, err8), exp8)

    def test_percentage_quantities_conversion_ff_and_pce(self):
        voc = OpenCircuitVoltage(value=[756.0], units=Volt(magnitude=-3.), raw_value='756.0', error=5.)
        jsc = ShortCircuitCurrentDensity(value=[15.49], units=AmpPerMeterSquared(magnitude=1.), raw_value='15.49', error= 1)
        ff = FillFactor(value=[0.664], units=Percent(powers=1), raw_value='0.664', raw_units='%)')
        pce = PowerConversionEfficiency(value=[0.05], units=Percent(powers=1), raw_value='0.05', raw_units='(%)')
        print(pce.raw_units)
        record = PhotovoltaicCell(voc=voc, jsc=jsc, ff=ff, pce=pce)

        updated_record = calculate_irradiance(record)
        output = updated_record.derived_properties['solar_simulator']
        self.assertEqual(output.value, [1600.0])
        self.assertEqual(output.error, 300.0)

    def test_percentage_quantities_conversion_ff_and_pce_without_units(self):
        voc = OpenCircuitVoltage(value=[756.0], units=Volt(magnitude=-3.), raw_value='756.0', error=5.)
        jsc = ShortCircuitCurrentDensity(value=[15.49], units=AmpPerMeterSquared(magnitude=1.), raw_value='15.49', error= 1)
        ff = FillFactor(value=[0.664], raw_value='0.664')
        pce = PowerConversionEfficiency(value=[0.05], raw_value='0.05', raw_units='(%)')
        print(pce.raw_units)
        record = PhotovoltaicCell(voc=voc, jsc=jsc, ff=ff, pce=pce)

        updated_record = calculate_irradiance(record)
        output = updated_record.derived_properties['solar_simulator']
        self.assertEqual(output.value, [160000.0])
        self.assertEqual(output.error, 30000.0)