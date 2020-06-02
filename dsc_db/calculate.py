"""
Functionality to calculate properties from extracted data
"""

from chemdataextractor.model.units.current import Ampere
from chemdataextractor.model.units.current_density import AmpPerMeterSquared
from chemdataextractor.model.units.area import MetersSquaredAreaUnit
from chemdataextractor.model.units.irradiance import WattPerMeterSquared
from chemdataextractor.model.units.power import Watt
from chemdataextractor.model.units.ratio import Percent
from chemdataextractor.model.units.resistance import Ohm
from chemdataextractor.model.pv_model import SimulatedSolarLightIntensity, ShortCircuitCurrentDensity, ShortCircuitCurrent, \
    SpecificChargeTransferResistance, SpecificSeriesResistance, ChargeTransferResistance,SeriesResistance, \
    PowerIn, PowerMax

from statistics import mean
from math import sqrt

import copy
import sigfig

hyphens = '-‐‑⁃‒–—―'


def calculate_metrics(record, active_area_record):
    """
    Calculate values of properties where possible
    :param records: List of PhotovoltaicCell object records

    """

    if active_area_record is not None:
        # Attempt to calculate current/current density properties
        try:
            record = calculate_current_density(record, active_area_record)
            record = calculate_current(record, active_area_record)

            record = calculate_specific_resistance_rct(record, active_area_record)
            record = calculate_specific_resistance_rs(record, active_area_record)
            record = calculate_resistance_rct(record, active_area_record)
            record = calculate_resistance_rs(record, active_area_record)
        except:
            print('Couldn\'t interpret units of active area. Not calculating this.')

    # Logic to caluclate irradiance
    record = calculate_irradiance(record)

    if active_area_record is not None:
        # Attempt to calculated power in and power max
        try:
            record = calculate_power_in(record, active_area_record)
            # record = calculate_power_max(record)
        except:
            print('Couldn\'t interpret units of active area. Not calculating this.')

    record = calculate_power_max(record)

    return record


def calculate_power_in(record, active_area_record):
    """
    Calculate the power in based of extracted properties. Where more than one value is given for a record, the average
    is taken.
    :param: List : records. List of chemical records from ChemDataExtractor
    """

    new_record = copy.deepcopy(record)
    if record.solar_simulator or 'solar_simulator' in record.calculated_properties.keys():
        solar_simulator = None
        # Use extracted solar_simulator value if possible
        if record.solar_simulator:
            if all([record.solar_simulator.value, record.solar_simulator.units]):
                solar_simulator = record.solar_simulator.units.convert_value_to_standard(mean(record.solar_simulator.value))

        # Otherwise, try to get calculated property
        if 'solar_simulator' in record.calculated_properties.keys() and solar_simulator is None:
            ss_obj = record.calculated_properties['solar_simulator']
            solar_simulator = ss_obj.units.convert_value_to_standard(mean(ss_obj.value))

        if solar_simulator is not None:
            active_area = mean(active_area_record['ActiveArea']['std_value'])

            pin = solar_simulator * active_area
            pin_err = calculate_power_in_error(record, active_area_record, solar_simulator, active_area, pin, quantity='solar_simulator')
            pin = round_to_sig_figs(pin, pin_err)

            pin_record = PowerIn(value=[pin], units=Watt(), error=pin_err)
            new_record.set_calculated_properties('pin', pin_record)

    return new_record


def calculate_power_max(record):
    """
    Calculate the maximum based of extracted properties. Where more than one value is given for a record, the average
    is taken.
    :param: List : records. List of chemical records from ChemDataExtractor
    """

    new_record = copy.deepcopy(record)
    if record.pce and (record.pin or 'pin' in record.calculated_properties.keys()):
        pin = None
        # Use extracted solar_simulator value if possible
        if record.pin:
            if all([record.pin.value, record.pin.units]):
                pin = record.pin.units.convert_value_to_standard(mean(record.pin.value))

        # Otherwise, try to get calculated property
        if 'pin' in record.calculated_properties.keys() and pin is None:
            pin_obj = record.calculated_properties['pin']
            pin = pin_obj.units.convert_value_to_standard(mean(pin_obj.value))

        if pin is not None and record.pce.value:
            # Calculate PCE (use the unit where given)
            pce_mean = mean(record.pce.value)
            if isinstance(record.pce.units, Percent):
                pce = pce_mean / 100

            # If decimal is larger than Shockley-Queisser limit, assume it is a percentage
            elif pce_mean > 0.34:
                pce = pce_mean / 100
            else:
                pce = pce_mean

            pmax = pin * pce
            pmax_err = calculate_power_max_error(record, pin, pce, pmax)
            pmax = round_to_sig_figs(pmax, pmax_err)

            pmax_record = PowerMax(value=[pmax], units=Watt(), error=pmax_err)
            new_record.set_calculated_properties('pmax', pmax_record)

    return new_record


def calculate_specific_resistance_rct(record, active_area_record):
    """
    Calculate the specific values of Rct when active area is identified
    """

    new_record = copy.deepcopy(record)
    if all([record.charge_transfer_resistance, active_area_record]):
        if all([record.charge_transfer_resistance.value, record.charge_transfer_resistance.units, active_area_record['ActiveArea']['std_value']]):

            rct = record.charge_transfer_resistance.units.convert_value_to_standard(mean(record.charge_transfer_resistance.value))
            active_area = mean(active_area_record['ActiveArea']['std_value'])

            sp_rct = rct * active_area
            sp_rct_err = calculate_resistance_error(record, active_area_record, rct, active_area, sp_rct, quantity='charge_transfer_resistance')
            sp_rct = round_to_sig_figs(sp_rct, sp_rct_err)

            sp_rct_record = SpecificChargeTransferResistance(value=[sp_rct], units=(Ohm() * MetersSquaredAreaUnit()), error=sp_rct_err)
            new_record.set_calculated_properties('specific_charge_transfer_resistance', sp_rct_record)

    return new_record


def calculate_specific_resistance_rs(record, active_area_record):
    """
    Calculate the specific values of Rs when active area is identified
    """

    new_record = copy.deepcopy(record)
    if all([record.series_resistance, active_area_record]):
        if all([record.series_resistance.value, record.series_resistance.units, active_area_record['ActiveArea']['std_value']]):

            rs = record.series_resistance.units.convert_value_to_standard(mean(record.series_resistance.value))
            active_area = mean(active_area_record['ActiveArea']['std_value'])

            sp_rs = rs * active_area
            sp_rs_err = calculate_resistance_error(record, active_area_record, rs, active_area, sp_rs, quantity='series_resistance')
            sp_rs = round_to_sig_figs(sp_rs, sp_rs_err)

            sp_rs_record = SpecificSeriesResistance(value=[sp_rs], units=(Ohm() * MetersSquaredAreaUnit()), error=sp_rs_err)
            new_record.set_calculated_properties('specific_series_resistance', sp_rs_record)

    return new_record


def calculate_resistance_rct(record, active_area_record):
    """
    Calculate the values of Rct when active area is identified and the specific resistances are given
    """

    new_record = copy.deepcopy(record)
    # First attempt to calculate the specific Rct value(sp_rct) when Rct given
    if all([record.specific_charge_transfer_resistance, active_area_record]):
        if all([record.specific_charge_transfer_resistance.value, record.specific_charge_transfer_resistance.units, active_area_record['ActiveArea']['std_value']]):

            sp_rct = record.specific_charge_transfer_resistance.units.convert_value_to_standard(mean(record.specific_charge_transfer_resistance.value))
            active_area = mean(active_area_record['ActiveArea']['std_value'])

            rct = sp_rct / active_area
            rct_err = calculate_resistance_error(record, active_area_record, sp_rct, active_area, rct, quantity='specific_charge_transfer_resistance')
            rct = round_to_sig_figs(rct, rct_err)

            rct_record = ChargeTransferResistance(value=[rct], units=Ohm(), error=rct_err)
            new_record.set_calculated_properties('charge_transfer_resistance', rct_record)

    return new_record


def calculate_resistance_rs(record, active_area_record):
    """
    Calculate the values of Rs when active area is identified and the specific resistances are given
    """

    new_record = copy.deepcopy(record)
    if all([record.specific_series_resistance, active_area_record]):
        if all([record.specific_series_resistance.value, record.specific_series_resistance.units, active_area_record['ActiveArea']['std_value']]):

            sp_rs = record.specific_series_resistance.units.convert_value_to_standard(mean(record.specific_series_resistance.value))
            active_area = mean(active_area_record['ActiveArea']['std_value'])

            rs = sp_rs / active_area
            rs_err = calculate_resistance_error(record, active_area_record, sp_rs, active_area, rs, quantity='specific_series_resistance')
            rs = round_to_sig_figs(rs, rs_err)

            rs_record = SeriesResistance(value=[rs], units=Ohm(), error=rs_err)
            new_record.set_calculated_properties('series_resistance', rs_record)

    return new_record


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
    try:
        if all([record.voc, record.ff, record.pce]) and (record.jsc or 'jsc' in record.calculated_properties.keys()):
            if all([record.voc.value, record.voc.units, record.ff.value, record.pce.value]):
                jsc = None
                # Use extracted jsc value if possible
                if record.jsc:
                    if all([record.jsc.value, record.jsc.units]):
                        jsc = record.jsc.units.convert_value_to_standard(mean(record.jsc.value))

                # Otherwise, try to get calculated property
                if 'jsc' in record.calculated_properties.keys() and jsc is None:
                    jsc_obj = record.calculated_properties['jsc']
                    jsc = jsc_obj.units.convert_value_to_standard(mean(jsc_obj.value))

                if jsc is not None:
                    voc = record.voc.units.convert_value_to_standard(mean(record.voc.value))

                    ff_mean = mean(record.ff.value)
                    if isinstance(record.ff.units, Percent):
                        ff = ff_mean / 100
                    else:
                        # If FF > 1, assume it is a percentage
                        if ff_mean > 1:
                            ff = ff_mean / 100
                        else:
                            ff = ff_mean

                    # Calculate PCE (use the unit where given)
                    pce_mean = mean(record.pce.value)
                    if isinstance(record.pce.units, Percent):
                        pce = pce_mean / 100

                    # If decimal is larger than Shockley-Queisser limit, assume it is a percentage
                    elif pce_mean > 0.34:
                        pce = pce_mean / 100
                    else:
                        pce = pce_mean

                    irr = calculate_irradiance_value(voc, jsc, ff, pce)
                    irr_err = calculate_irradiance_error(record, voc, jsc, ff, pce, irr)
                    irr = round_to_sig_figs(irr, irr_err)

                    solar_sim = SimulatedSolarLightIntensity(value=[irr], units=WattPerMeterSquared(), error=irr_err)
                    new_record.set_calculated_properties('solar_simulator', solar_sim)
    except:
        print('Unsupported raw value format, could not calculate the solar_simulator')

    return new_record


def round_to_sig_figs(irr, irr_err):
    """
    Round the irradiance to the appropriate number of significant figures
    """
    return sigfig.round(irr, uncertainty=irr_err)


def calculate_power_in_error(record, aa_record, input, active_area, output, quantity):

    input_error = calc_error_quantity(record, quantity)
    active_area_error = calc_error_active_area(aa_record)

    # Calculate the error on output quantity
    output_error = output * sqrt(((input_error / input) ** 2) + ((active_area_error / active_area) ** 2))
    # Round to one s.f
    return sigfig.round(output_error, sigfigs=1)


def calculate_power_max_error(record, pin, pce, pmax):
    """
    Calculate the error for power max quantity
    """

    pin_error = calc_error_quantity(record, 'pin')
    pce_error = calc_error_quantity(record, 'pce')

    # Calculate the error on output quantity
    pmax_error = pmax * sqrt(((pin_error / pin) ** 2) + ((pce_error / pce) ** 2))
    # Round to one s.f
    return sigfig.round(pmax_error, sigfigs=1)


def calculate_resistance_error(record, aa_record, input_r, active_area, output_r, quantity):

    input_r_error = calc_error_quantity(record, quantity)
    active_area_error = calc_error_active_area(aa_record)

    # Calculate the jsc error
    output_r_error = output_r * sqrt(((input_r_error / input_r) ** 2) + ((active_area_error / active_area) ** 2))
    # Round to one s.f
    return sigfig.round(output_r_error, sigfigs=1)


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

    if 'cm2' in active_area['raw_units']:
        prop_calc_error = MetersSquaredAreaUnit(magnitude=-4).convert_value_to_standard(prop_calc_raw_error)
    elif 'mm2' in active_area['raw_units']:
        prop_calc_error = MetersSquaredAreaUnit(magnitude=-6).convert_value_to_standard(prop_calc_raw_error)
    elif 'm2' in active_area['raw_units']:
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

    potentially_calculated_fields = ['jsc', 'solar_simulator', 'pin']

    # Choose the calculated property for jsc if required
    if field in potentially_calculated_fields:
        if getattr(record, field) is not None:
            rec = getattr(record, field)
        elif field in record.calculated_properties.keys():
            rec = record.calculated_properties[field]
    else:
        rec = getattr(record, field)

    if rec.error is not None:
        prop_calc_raw_error = rec.error
    else:
        prop_calc_raw_error = estimate_error_from_length_of_raw_value_string(rec)
    if field in ['voc', 'isc', 'jsc', 'charge_transfer_resistance', 'specific_charge_transfer_resistance',
                 'series_resistance', 'specific_series_resistance', 'solar_simulator', 'pin', 'pmax']:
        prop_calc_error = rec.units.convert_value_to_standard(prop_calc_raw_error)
    elif field == 'ff':
        if mean(record.ff.value) > 1 or isinstance(record.ff.units, Percent):
            prop_calc_error = prop_calc_raw_error / 100
        else:
            prop_calc_error = prop_calc_raw_error
    elif field == 'pce':
        if isinstance(record.pce.units, Percent) or mean(record.pce.value) > 0.34:
            prop_calc_error = prop_calc_raw_error / 100
        else:
            prop_calc_error = prop_calc_raw_error
    else:
        print('Unrecognized quantity.')
        raise Exception

    return prop_calc_error


def estimate_error_from_length_of_raw_value_string(rec):
    """
    Estimate the raw error on a value from the number of characters given
    """

    raw_value = rec.raw_value
    error_string = ''

    # Begin by checking for presence of minus/hyphen symbol
    used_hyphens = [char for char in hyphens if char in raw_value]
    if len(used_hyphens) == 1:
        if raw_value[0] != used_hyphens[0] and raw_value.count(used_hyphens[0]) == 1:
            # Assume ranged quantity, split at hyphen
            value1, value2 = raw_value.split(used_hyphens[0])
            # Choose the quantity with less sig_figs
            if len(value1.replace('.', '')) > len(value2.replace('.', '')):
                raw_value = value2
            else:
                raw_value = value1
        elif raw_value[0] == used_hyphens[0] and raw_value.count(used_hyphens[0]) == 1:
            # Case for a negative number
            raw_value = raw_value[1:]
    elif len(used_hyphens) == 2: # Assuming that one hyphen describes negativity, and one the ranged quantity
        if raw_value[0] in used_hyphens:
            neg_hyphen = raw_value[0]
            used_hyphens.remove(neg_hyphen)
            raw_value = raw_value.replace(neg_hyphen, '')

            # Assume ranged quantity, split at hyphen
            value1, value2 = raw_value.split(used_hyphens[0])
            # Choose the quantity with less sig_figs
            if len(value1.replace('.', '')) > len(value2.replace('.', '')):
                raw_value = value2
            else:
                raw_value = value1
        else:
            raise Exception('Two hyphens detected in raw value, but couldn\'t parse...')

    elif used_hyphens != []:
        raise Exception('Multiple hyphens detected in raw value. Couldn\'t parse...')

    for char in raw_value[:-1]:
        if char != '.':
            error_string += '0'
        else:
            error_string += '.'
    error_string += '1'

    return float(error_string)


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


def calculate_relative_metrics_perovskite(records):
    """
    Calculate relative metrics for standard properties of perovskites
    Experiments typically express their results (for example, with a novel counter electrode) alongside the standard
    setup for this (for example, a platinum (Pt) counter electrode). This is done as the values of each property can
    vary across experiment, so this provides a baseline to compare the values from the particular experiment to.

    This function will attempt to determine whether the independent variable is one that can be standardized. If it is,
    and the standard comparison is also present, the value is calculated.    """

    #start by classifying the table
    classification, relative_record = classify_table_perovskite(records)

    if classification != 'None':
        records = calculate_relative_efficiencies_perovskite(records, relative_record, classification )
    return records


def classify_table(records):
    """
    Classify the table by looking at variables
    """

    # Test for counter electrode
    classification, ref_record = do_classification(records, 'counter_electrode', 'CounterElectrode', 'Pt')
    if classification == 'None':
        # Test for DSC. First check for N719
        classification, ref_record = do_classification(records, 'dye', 'Dye', 'N719')
        if classification == 'None':
            # Next check for DSC with reference N3
            classification, ref_record = do_classification(records, 'dye', 'Dye', 'N3')
            if classification == 'None':
                    # Test for semiconductor
                    classification, ref_record = do_classification(records, 'semiconductor', 'Semiconductor', 'TiO2')

    return classification, ref_record


def classify_table_perovskite(records):
    """
    Classify the perovskite table by looking at the variables
    """

    # Test for counter electrode
    classification, ref_record = do_classification(records, 'perovskite', 'Perovskite', 'CH3NH3PbI3')
    # TODO - Add list of other useful relative variables here...

    return classification, ref_record


def do_classification(records, field_name, model_name, ref_value):
    """
    Identify candidates for referencing
    """

    if all([field in record.keys() for record in records for field in (field_name, 'pce')]):

        # Check that records contain a name for the targetted property and a value for pce
        if all(['raw_value' in record[field_name][model_name].keys() for record in records]) and \
                all(['value' in record['pce']['PowerConversionEfficiency'].keys() for record in records]):

            # Determine if all values are unique, and which is the reference result.
            unique_values = set()
            ref_record = None
            for record in records:
                unique_values.add(record[field_name][model_name]['raw_value'])
                if record[field_name][model_name]['raw_value'].replace(' ', '') == ref_value:
                    ref_record = record

            if len(unique_values) == len(records) and ref_record is not None:
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
        if pt_record['dye']['Dye']['raw_value'].replace(' ', '') == 'N719':
            std_component = 'N719'
        else:
            std_component = 'N3'
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


def calculate_relative_efficiencies_perovskite(records, pt_record, classification):
    """
    Calculate the relative efficiencies for an appropriate table
    Assumes that the units of the PCE will be consistent throughout the table.
    """

    # Determine the standard component
    # TODO: Expand this to account for all properties that could benefit from relative metrics 
    #    (this may become apparent after testing)
    if classification == 'perovskite':
        std_component = 'CH3NH3PbI3'
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

