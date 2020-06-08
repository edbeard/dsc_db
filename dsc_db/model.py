"""
Model classes for Photovoltaic records

Valid results must include a dye and at least one photovoltaic property
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import six


class PhotovoltaicRecord(object):
    """

    """
    _fields = ['jsc', 'isc', 'voc', 'pce', 'ff', 'dye', 'ref', 'redox_couple', 'dye_loading', 'counter_electrode',
               'semiconductor', 'active_area', 'solar_simulator', 'electrolyte', 'substrate',
               'charge_transfer_resistance', 'series_resistance', 'specific_charge_transfer_resistance',
               'specific_series_resistance', 'exposure_time', 'table_row_categories', 'calculated_properties', 'pin', 'pmax']

    def __init__(self, records, table=None):
        # Initialize exisiting records
        missing_fields = []
        for key, value in six.iteritems(records):
            if key in ['series_resistance', 'charge_transfer_resistance', 'specific_series_resistance', 'specific_charge_transfer_resistance' ]:
                if 'units' not in next(iter(value.values())).keys():
                   # print('No unit extracted for record : %s' % value)
                    missing_fields.append(key)
                else:
                    setattr(self, key, value)
            else:
                setattr(self, key, value)
        # Set default values to None
        missing_fields += [field for field in self._fields if field not in records.keys()]
        for field in missing_fields:
            setattr(self, field, None)

        # Adjust dye field to be in a list format if found...
        if self.dye is not None:
            if type(self.dye['Dye']) is not list:
                dye_updated = {'Dye': [self.dye['Dye']]}
                setattr(self, 'dye', dye_updated)

        # Set table that was extracted
        self.table = table

    def __repr__(self):
        string = 'PV record with dye: ' + str(self.dye) + ', '
        string += 'and a Voc of ' + str(self.voc)
        return string

    def __str__(self):
        string = 'PV record with dye: ' + str(self.dye) + ', '
        string += 'and a Voc of ' + str(self.voc)
        return string
    def __contains__(self, name):
        try:
            val = getattr(self, name)
            return val is not None
        except AttributeError:
            return False

    def serialize(self, primitive=False, include_none=False):
        """Convert Model to python dictionary."""
        # Serialize fields to a dict
        data = {}
        for field_name in self._fields:
            value = getattr(self, field_name)
            # Skip empty fields unless field.null
            if not include_none:
                if value in [None, '', []]:
                    continue
            data[field_name] = value
        return data

    def _substitute_definitions(self, fieldstr, model, doc):
        """ Generic function to substitute abbreviations into chemical records for a PhotovoltaicCell object.
                NOTE: This logic compares the raw_value of a model to the abbreviations provided

            :param Model : String containing the name of the model
            :param field : String containing the name of the field to be replaced
        """

        # abbreviations = self.doc.abbreviation_definitions
        abbreviations = [(abbr, defs) for abbrs, defs, _ in doc.abbreviation_definitions for abbr in abbrs]

        field = getattr(self, fieldstr)

        for abbr, defs in abbreviations:

            # Check when the field is a list
            if type(field[model]) == list:
                for i, model_inst in enumerate(field[model]):
                    if 'raw_value' in field[model][i]:
                        if field[model][i]['raw_value'] == abbr and 'abbreviations' not in field.keys():
                            field[model][i].update({'abbreviations': [defs]})
                        elif field[model][i]['raw_value'] == abbr:
                            field[model][i]['abbreviations'].append(defs)

            # When not a list, update the abbreviations separately...
            elif 'raw_value' in field[model]:
                if field[model]['raw_value'] == abbr and 'abbreviations' not in field.keys():
                    field[model].update({'abbreviations': [defs]})
                elif field[model]['raw_value'] == abbr:
                    field[model]['abbreviations'].append(defs)

        setattr(self, fieldstr, field)

    def _substitute_compound(self, fieldstr, model, compound_records):
        """ Generic function to substitute compounds into chemical records for a PhotovoltaicCell object.
                NOTE: This logic compares the raw_value of a model to the abbreviations provided

            :param abbreviations : List of chemical abbreviations
            :param Model : String containing the name of the model
            :param field : String containing the name of the field to be replaced
            :param compound_records: Compound records for the entire document
        """

        field = getattr(self, fieldstr)

        # Substitute values (different for list attributes)
        for compound in compound_records:

            # Check for matches to the chemical name
            if 'names' in compound.keys():
                names = compound['names']

                # Check when the field is a list
                if type(field[model]) == list:
                    for i, model_inst in enumerate(field[model]):
                        if 'raw_value' in model_inst.keys():
                            if model_inst['raw_value'] in names and 'compound' not in field.keys():
                                field[model][i].update({'compound': compound})
                # Check when the field is a single value
                elif 'raw_value' in field[model]:
                    if 'compound' not in field.keys() and field[model]['raw_value'] in names:
                        field[model].update({'compound': compound})

            # Check for matches to the chemical label
            if 'labels' in compound.keys():
                labels = compound['labels']

                # Check when the field is a list
                if type(field[model]) == list:
                    for i, model_inst in enumerate(field[model]):
                        if 'raw_value' in model_inst.keys():
                            if model_inst['raw_value'] in labels and 'compound' not in field.keys():
                                field[model][i].update({'compound': compound})
                # Check when the field is a single value
                elif 'raw_value' in field[model]:
                    if 'compound' not in field.keys() and field[model]['raw_value'] in labels:
                        field[model].update({'compound': compound})

        setattr(self, fieldstr, field)


class PerovskiteRecord(PhotovoltaicRecord):

    _fields = ['jsc', 'isc', 'voc', 'pce', 'ff', 'ref', 'perovskite', 'etl', 'htl',
               'counter_electrode', 'active_area', 'solar_simulator', 'substrate',
               'charge_transfer_resistance', 'series_resistance', 'exposure_time', 'specific_charge_transfer_resistance',
                'specific_series_resistance', 'exposure_time', 'table_row_categories', 'calculated_properties',
               'pin', 'pmax']

    def __init__(self, records, table=None):
        # Initialize exisiting records
        for key, value in six.iteritems(records):
            setattr(self, key, value)
        # Set default values to None
        missing_fields = [field for field in self._fields if field not in records.keys()]
        for field in missing_fields:
            setattr(self, field, None)

        # Adjust dye field to be in a list format if found...
        # if self.dye is not None:
        #     if type(self.dye['Dye']) is not list:
        #         dye_updated = {'Dye': [self.dye['Dye']]}
        #         setattr(self, 'dye', dye_updated)

        # Set table that was extracted
        self.table = table

    def __repr__(self):
        string = 'PV record with perovskite:' + str(self.perovskite) + ', '
        string += 'and a Voc of ' + str(self.voc)
        return string

    def __str__(self):
        string = 'PV record with perovskite:' + str(self.perovskite) + ', '
        string += 'and a Voc of ' + str(self.voc)
        return string