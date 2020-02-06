"""
Model classes for Photovoltaic records

Valid results must include a dye and at least one photovoltaic property
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import six


class PhotovoltaicRecord(object):
    """

    """
    _fields = ['jsc', 'voc', 'pce', 'ff', 'dye', 'ref', 'redox_couple', 'dye_loading', 'counter_electrode',
               'semiconductor', 'active_area', 'solar_simulator', 'electrolyte', 'substrate',
               'charge_transfer_resistance', 'series_resistance', 'exposure_time']

    def __init__(self, records, doc=None, table=None):
        # Initialize exisiting records
        for key, value in six.iteritems(records):
            setattr(self, key, value)
        # Set default values to None
        missing_fields = [field for field in self._fields if field not in records.keys()]
        for field in missing_fields:
            setattr(self, field, None)
        # Set associated document
        self.doc = doc

        # Set table that was extracted
        self.table = table


    def __repr__(self):
        return '<%s>' % (self.__class__.__name__,)

    def __str__(self):
        return '<%s>' % (self.__class__.__name__,)

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

    def _substitute_definitions(self, fieldstr, model):
        """ Generic function to substitute abbreviations into chemical records for a PhotovoltaicCell object.
                NOTE: This logic compares the raw_value of a model to the abbreviations provided

            :param Model : String containing the name of the model
            :param field : String containing the name of the field to be replaced
        """

        # abbreviations = self.doc.abbreviation_definitions
        abbreviations = [(abbr, defs) for abbrs, defs, _ in self.doc.abbreviation_definitions for abbr in abbrs]

        field = getattr(self, fieldstr)
        for abbr, defs in abbreviations:
            if field[model]['raw_value'] == abbr:
                if 'abbreviations' not in field.keys():
                    field[model].update({'abbreviations': [defs]})
                else:
                    field[model]['abbreviations'].append(defs)
        setattr(self, fieldstr, field)

    def _substitute_compound(self, fieldstr, model):
        """ Generic function to substitute compounds into chemical records for a PhotovoltaicCell object.
                NOTE: This logic compares the raw_value of a model to the abbreviations provided

            :param abbreviations : List of chemical abbreviations
            :param Model : String containing the name of the model
            :param field : String containing the name of the field to be replaced
        """

        doc_records = [record.serialize() for record in self.doc.records]
        compound_records = [record['Compound'] for record in doc_records if 'Compound' in record.keys()]
        compound_names = [(compound['names'], compound) for compound in compound_records if 'names' in compound.keys()]

        field = getattr(self, fieldstr)
        for names, compound in compound_names:
            if field[model]['raw_value'] in names:
                if 'compound' not in field.keys():
                    field[model].update({'compound': compound})

        setattr(self, fieldstr, field)



