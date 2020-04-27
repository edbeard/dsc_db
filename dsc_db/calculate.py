"""
Functionality to calculate properties from extracted data
"""

from chemdataextractor.model.units.current_density import CurrentDensityModel, CurrentDensityUnit
from chemdataextractor.model.units.irradiance import WattPerMeterSquared
from chemdataextractor.model.pv_model import SimulatedSolarLightIntensity

from statistics import mean


def calculate_metrics(record):
    """
    Calculate values of properties where possible
    :param records: List of PhotovoltaicCell object records

    """
    record = calculate_irradiance(record)
    return record


def calculate_irradiance(record):
    """
    Calculate the irradiance based of extracted properties. Where more than one value is given for a record, the average
    is taken.
    :param: List : records. List of chemical records from ChemDataExtractor
    """

    if all([record.voc, record.jsc, record.ff, record.pce]):
        if all([record.voc.value, record.voc.units, record.jsc.value, record.jsc.units, record.ff.value, record.pce.value]):

            voc = record.voc.units.convert_value_to_standard(mean(record.voc.value))
            jsc = record.jsc.units.convert_value_to_standard(mean(record.jsc.value))
            ff_mean = mean(record.ff.value)
            pce_mean = mean(record.pce.value)

            # If FF > 1, assume it is a percentage
            if ff_mean > 1:
                ff = ff_mean / 100
            else:
                ff = ff_mean

            # Calculate PCE (use the unit where given)
            if record.pce.units or pce_mean > 1:
                pce = pce_mean / 100
            else:
                pce = pce_mean

            irr = calculate_irradiance_value(voc, jsc, ff, pce)
            record.calculated_properties['solar_simulator'] = SimulatedSolarLightIntensity(value=[round(irr, 1)], units=WattPerMeterSquared())
            print('voc value: %s, jsc value: %s, ff value: %s, pce value: %s' % (voc, jsc, ff, pce))
            print('calculated irradiance: %s' % irr)

    return record


def calculate_irradiance_value(voc, jsc, ff, pce):
    return (voc * jsc * ff) / pce
