"""
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import unittest

from dsc_db.model import PhotovoltaicRecord
from dsc_db.run import add_distributor_info

from chemdataextractor.doc import Table, Caption


class TestData(unittest.TestCase):

    def test_add_distributor_info(self):

        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'dye': {'Dye': [{'raw_value': 'XY1', 'specifier': 'dye'}]}
        }
        expected = {'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc', 'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
                    'dye': {'Dye': [{'raw_value': 'XY1', 'specifier': 'dye',
                                     'smiles': 'CCCCC(CC)COc1ccc(c(OCC(CC)CCCC)c1)c2ccc(cc2)N(c3ccc(cc3)c4ccc(OCC(CC)CCCC)cc4OCC(CC)CCCC)c5ccc(cc5)c6ccc(c7sc8c9sc(cc9C(CC(CC)CCCC)(CC(CC)CCCC)c8c7)c%10ccc(cc%10)\\C=C(C#N)\\C(O)=O)c%11nsnc6%11',
                                     'name': "(E)-3-(4-(6-(7-(4-(bis(2',4'-bis((2-ethylhexyl)oxy)-[1,1'-biphenyl]-4-yl)amino)phenyl)benzo[c][1,2,5]thiadiazol-4-yl)-4,4-bis(2-ethylhexyl)-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)phenyl)-2-cyanoacrylic acid",
                                     'labels': ['DN-F16', 'XY1', "(E)-3-(4-(6-(7-(4-(bis(2',4'-bis((2-ethylhexyl)oxy)-[1,1'-biphenyl]-4-yl)amino)phenyl)benzo[c][1,2,5]thiadiazol-4-yl)-4,4-bis(2-ethylhexyl)-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)phenyl)-2-cyanoacrylic acid"]}]}}

        pv_records = [PhotovoltaicRecord(input, Table(Caption("")))]
        pv_records = add_distributor_info(pv_records)
        self.assertEqual(pv_records[0].serialize(), expected)
