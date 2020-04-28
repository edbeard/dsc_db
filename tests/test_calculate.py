"""
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import unittest

from dsc_db.model import PhotovoltaicRecord
from dsc_db.calculate import calculate_metrics, calculate_irradiance
from pprint import pprint

from chemdataextractor import Document
from chemdataextractor.model import Compound
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

