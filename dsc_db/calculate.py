"""
Functionality to calculate properties from extracted data
"""

from chemdataextractor.model.units.current import Ampere
from chemdataextractor.model.units.current_density import AmpPerMeterSquared
from chemdataextractor.model.units.area import MetersSquaredAreaUnit
from chemdataextractor.model.units.irradiance import WattPerMeterSquared
from chemdataextractor.model.pv_model import SimulatedSolarLightIntensity, ShortCircuitCurrentDensity, ShortCircuitCurrent

from statistics import mean
from math import sqrt

import copy
import sigfig


def calculate_metrics(record, active_area_record):
    """
    Calculate values of properties where possible
    :param records: List of PhotovoltaicCell object records

    """

    if active_area_record is not None:
        try:
            record = calculate_current_density(record, active_area_record)
            record = calculate_current(record, active_area_record)
        except:
            print('Couldn\'t interpret units of active area. Not calculating this.')
    record = calculate_irradiance(record)
    return record


def calculate_current_density(record, active_area_record):
    """
    Calculate the short circuit current density when the active area is given
    """

    new_record = copy.deepcopy(record)
    # First, attempt to calculate the Jsc when Isc given
    if all([record.isc, active_area_record]):
        if all([record.isc.value, record.isc.units, active_area_record['ActiveArea']['std_value']]):

            isc = record.isc.units.convert_value_to_standard(mean(record.isc.value))
            active_area = mean(active_area_record['ActiveArea']['std_value'])

            jsc = isc / active_area
            jsc_err = calculate_jsc_error(record, active_area_record, isc, active_area, jsc)
            jsc = round_to_sig_figs(jsc, jsc_err)

            short_circuit_current_density = ShortCircuitCurrentDensity(value=[jsc], units=AmpPerMeterSquared(), error=jsc_err)
            new_record.set_calculated_properties('jsc', short_circuit_current_density)

    return new_record


def calculate_current(record, active_area_record):
    """
    Calculate the short circuit current when the active area is given
    """

    new_record = copy.deepcopy(record)
    # First, attempt to calculate the Jsc when Isc given
    if all([record.jsc, active_area_record]):
        if all([record.jsc.value, record.jsc.units, active_area_record['ActiveArea']['std_value']]):

            jsc = record.jsc.units.convert_value_to_standard(mean(record.jsc.value))
            active_area = mean(active_area_record['ActiveArea']['std_value'])

            isc = jsc * active_area
            isc_err = calculate_isc_error(record, active_area_record, jsc, active_area, isc)
            isc = round_to_sig_figs(isc, isc_err)

            short_circuit_current = ShortCircuitCurrent(value=[isc], units=Ampere(), error=isc_err)
            new_record.set_calculated_properties('isc', short_circuit_current)

    return new_record


def calculate_irradiance(record):
    """
    Calculate the irradiance based of extracted properties. Where more than one value is given for a record, the average
    is taken.
    :param: List : records. List of chemical records from ChemDataExtractor
    """
    new_record = copy.deepcopy(record)
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
            if record.pce.units or pce_mean > 0.35:
                pce = pce_mean / 100
            else:
                pce = pce_mean

            irr = calculate_irradiance_value(voc, jsc, ff, pce)
            irr_err = calculate_irradiance_error(record, voc, jsc, ff, pce, irr)
            irr = round_to_sig_figs(irr, irr_err)

            solar_sim = SimulatedSolarLightIntensity(value=[irr], units=WattPerMeterSquared(), error=irr_err)
            new_record.set_calculated_properties('solar_simulator', solar_sim)

    return new_record


def round_to_sig_figs(irr, irr_err):
    """
    Round the irradiance to the appropriate number of significant figures
    """
    return sigfig.round(irr, uncertainty=irr_err)


def calculate_irradiance_error(record, voc, jsc, ff, pce, irr):
    """
    Estimate the accuracy of the calculated data.
    """

    # Estimate the errors based on significant figure information
    voc_err = calc_error_quantity(record, 'voc')
    jsc_err = calc_error_quantity(record, 'jsc')
    ff_err = calc_error_quantity(record, 'ff')
    pce_err = calc_error_quantity(record, 'pce')

    # Calculate the irradiance error
    irr_err = irr * sqrt( ((voc_err / voc) ** 2) +  ((jsc_err / jsc) ** 2) + ((ff_err / ff) ** 2 + ((pce_err / pce) ** 2)))

    # Round to one s.f
    return sigfig.round(irr_err, sigfigs=1)


def calculate_jsc_error(record, aa_record, isc, active_area, jsc):
    """
    Estimate the accuracy of the calculated data.
    """

    isc_error = calc_error_quantity(record, 'isc')
    active_area_error = calc_error_active_area(aa_record)

    # Calculate the jsc error
    jsc_err = jsc * sqrt( ((isc_error / isc) ** 2) +  ((active_area_error / active_area) ** 2))
    # Round to one s.f
    return sigfig.round(jsc_err, sigfigs=1)


def calculate_isc_error(record, aa_record, jsc, active_area, isc):
    """
    Estimate the accuracy of the calculated data.
    """

    jsc_error = calc_error_quantity(record, 'jsc')
    active_area_error = calc_error_active_area(aa_record)

    # Calculate the jsc error
    isc_err = isc * sqrt( ((jsc_error / jsc) ** 2) +  ((active_area_error / active_area) ** 2))
    # Round to one s.f
    return sigfig.round(isc_err, sigfigs=1)


def calc_error_active_area(active_area_rec):
    """
    Calculate the error of active area from serialized record.
    If not available, estimate from the number of dp.
    """
    active_area = active_area_rec['ActiveArea']
    if 'error' in active_area.keys():
        prop_calc_raw_error = active_area['error']
    else:
        raw_value = active_area['raw_value']
        error_string = ''
        for char in raw_value[:-1]:
            if char != '.':
                error_string += '0'
            else:
                error_string += '.'
        error_string += '1'
        prop_calc_raw_error = float(error_string)

    if active_area['raw_units'] == 'cm2':
        prop_calc_error = MetersSquaredAreaUnit(magnitude=-4).convert_value_to_standard(prop_calc_raw_error)
    elif active_area['raw_units'] == 'mm2':
        prop_calc_error = MetersSquaredAreaUnit(magnitude=-6).convert_value_to_standard(prop_calc_raw_error)
    elif active_area['raw_units'] == 'm2':
        prop_calc_error = MetersSquaredAreaUnit(magnitude=0).convert_value_to_standard(prop_calc_raw_error)
    else:
        raise Exception('Couldn\'t identify units from active area')

    return prop_calc_error


def calc_error_quantity(record, field):
    """
    Calculate the error for a quantity, estimating where no error is given.
    First, the record is checked for an extracted error value.
    If not available, this is done by looking at the significant figures
    """

    if getattr(record, field).error is not None:
        prop_calc_raw_error = getattr(record, field).error
    else:
        raw_value = getattr(record, field).raw_value
        error_string = ''
        for char in raw_value[:-1]:
            if char != '.':
                error_string += '0'
            else:
                error_string += '.'
        error_string += '1'
        prop_calc_raw_error = float(error_string)
    if field in ['voc', 'jsc', 'isc']:
        prop_calc_error = getattr(record, field).units.convert_value_to_standard(prop_calc_raw_error)
    elif field == 'ff':
        if mean(record.ff.value) > 1:
            prop_calc_error = prop_calc_raw_error / 100
        else:
            prop_calc_error = prop_calc_raw_error
    elif field == 'pce':
        if record.pce.units or mean(record.pce.value) > 0.35:
            prop_calc_error = prop_calc_raw_error / 100
        else:
            prop_calc_error = prop_calc_raw_error
    else:
        print('Unrecognized quantity.')
        raise Exception

    return prop_calc_error


def calculate_irradiance_value(voc, jsc, ff, pce):
    # Calculate the irradiance taking into account the errors
    return (voc * jsc * ff) / pce


def calculate_relative_metrics(records):
    """
    Calculate relative metrics for standard properties.
    Experiments typically express their results (for example, with a novel counter electrode) alongside the standard
    setup for this (for example, a platinum (Pt) counter electrode). This is done as the values of each property can
    vary across experiment, so this provides a baseline to compare the values from the particular experiment to.

    This function will attempt to determine whether the independent variable is one that can be standardized. If it is,
    and the standard comparison is also present, the value is calculated.
    """

    # Start by classifying the table
    classification, relative_record = classify_table(records)

    if classification != 'None':
        records = calculate_relative_efficiencies(records, relative_record, classification )
    return records


def classify_table(records):
    """
    Classify the table by looking at variables
    """

    # Test for counter electrode
    classification, ref_record = do_classification(records, 'counter_electrode', 'CounterElectrode', 'Pt')
    if classification == 'None':
        # Test for DSC
        classification, ref_record = do_classification(records, 'dye', 'Dye', 'N719')
        if classification == 'None':
            # Test for semiconductor
            classification, ref_record = do_classification(records, 'semiconductor', 'Semiconductor', 'TiO2')

    return classification, ref_record


def do_classification(records, field_name, model_name, ref_value):
    """
    Identify candidates for referencing
    """

    if all([field in record.keys() for record in records for field in (field_name, 'pce')]):

        # Check that these values have names for the counter electrode and a value for the pce field_name
        if all(['raw_value' in record[field_name][model_name].keys() for record in records]) and \
                all(['value' in record['pce']['PowerConversionEfficiency'].keys() for record in records]):

            # Determine if all the counter electrode values are unique, and which is the reference result.
            unique_counter_electrodes = set()
            ref_record = None
            for record in records:
                unique_counter_electrodes.add(record[field_name][model_name]['raw_value'])
                if record[field_name][model_name]['raw_value'].strip(' ') == ref_value:
                    ref_record = record

            if len(unique_counter_electrodes) == len(records) and ref_record is not None:
                return field_name, ref_record

    return 'None', None


def calculate_relative_efficiencies(records, pt_record, classification):
    """
    Calculate the relative efficiencies for an appropriate table
    Assumes that the units of the PCE will be consistent throughout the table.
    """

    # Determine the standard component
    if classification == 'counter_electrode':
        std_component = 'Pt'
    elif classification == 'dye':
        std_component = 'N719'
    elif classification == 'semiconductor':
        std_component = 'TiO2'
    else:
        raise Exception

    baseline_efficiency = mean(pt_record['pce']['PowerConversionEfficiency']['value'])

    # Add a field to each record for efficiency
    for record in records:
        rec_efficiency = mean(record['pce']['PowerConversionEfficiency']['value'])
        relative_efficiency = rec_efficiency / baseline_efficiency
        normalized_data = {'value': relative_efficiency, 'component_name': classification, 'std_component': std_component}
        record['pce']['PowerConversionEfficiency']['normalized'] = normalized_data

    return records


