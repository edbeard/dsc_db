"""
Functionality to calculate properties from extracted data
"""

from chemdataextractor.model.units.current_density import CurrentDensityModel, CurrentDensityUnit
from chemdataextractor.model.units.irradiance import WattPerMeterSquared
from chemdataextractor.model.pv_model import SimulatedSolarLightIntensity

from statistics import mean

import copy


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
            solar_sim = SimulatedSolarLightIntensity(value=[round(irr, 1)], units=WattPerMeterSquared())
            new_record.set_calculated_properties('solar_simulator', solar_sim)

    return new_record


def calculate_irradiance_value(voc, jsc, ff, pce):
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

    if classification == 'counter_electrode':
        records = calculate_relative_efficiencies_counter_electrodes(records, relative_record)
    elif classification == 'dye':
        # Add logic for relative dye values...
        pass
    return records



def classify_table(records):
    """
    Classify the table by looking at variables
    """

    # If all records have a counter electrode property
        # If all records are unique

    # Determine if all records have a counter electrode and pce field.
    if all([field in record.keys() for record in records for field in ('counter_electrode', 'pce')]):
        print('all records have a counter electrode property and a pce value.')

        # Check that these values have names for the counter electrode and a value for the pce field
        if all(['raw_value' in record['counter_electrode']['CounterElectrode'].keys() for record in records]) and \
                all(['value' in record['pce']['PowerConversionEfficiency'].keys() for record in records]):
            print('All records have a raw_value and value property for ce and pce respectively.')

            # Determine if all the counter electrode values are unique, and which is the reference result.
            unique_counter_electrodes = set()
            pt_record = None
            for record in records:
                unique_counter_electrodes.add(record['counter_electrode']['CounterElectrode']['raw_value'])
                if record['counter_electrode']['CounterElectrode']['raw_value'].strip(' ') == 'Pt':
                    pt_record = record

            #
            if len(unique_counter_electrodes) == len(records) and pt_record is not None:
                print('Every CE result is unique and the reference value has been found.')
                return ('counter_electrode', pt_record)

    # Add an elif here to classify by dye etc.
    return 'None', None


def calculate_relative_efficiencies_counter_electrodes(records, pt_record):
    """
    Calculate the relative efficiencies for a table that contains counter electrode information.
    Assumes that the units of the PCE will be consistent throughout the table.
    """

    baseline_efficiency = mean(pt_record['pce']['PowerConversionEfficiency']['value'])
    print('The baseline efficiency is: %s' % baseline_efficiency)

    # Add a field to each record for
    for record in records:
        rec_efficiency = mean(record['pce']['PowerConversionEfficiency']['value'])
        relative_efficiency = rec_efficiency / baseline_efficiency
        print('The record efficiency is found to be: %s ' % rec_efficiency)
        print('This relative efficiency was found to be: %s' % relative_efficiency)
        record['pce']['PowerConversionEfficiency']['normalized_value'] = relative_efficiency

    return records


