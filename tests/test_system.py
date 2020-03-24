"""
System tests evaluating the pipeline on a larger scale
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import unittest

from chemdataextractor.doc import Sentence, Document, Caption, Paragraph
from chemdataextractor.doc.table import Table
from chemdataextractor.model.pv_model import CommonSentenceDye, PhotovoltaicCell

from dsc_db.run import get_table_records, add_dye_information
from dsc_db.model import PhotovoltaicRecord


class TestSystem(unittest.TestCase):

    def test_common_dye_detector(self):

        text_input = Paragraph(
            'A layer of TiO2 colloid film with a thickness of 10 μm and area of 0.25 cm2 was prepared by a sol–hydrothermal method and subsequently calcined at 450 °C for 30 min .'
            'The resultant TiO2 nanocrystalline film was sensitized by immersing into a 0.50 mM ethanol solution of N719 dye (purchased from DYESOL LTD) for 24 h.'
            'A DSSC device was fabricated by sandwiching redox electrolyte between a dye–sensitized TiO2 anode and a PVDF–implanted Co–Pt alloy CE.'
            'A redox electrolyte consisted of 100 mM of tetraethylammonium iodide, 100 mM of tetramethylammonium iodide, 100 mM of tetrabutylammonium iodide, 100 mM of NaI, 100 mM of KI, 100 mM of LiI, 50 mM of I2, and 500 mM of 4–tert–butyl–pyridine in 50 ml acetonitrile .'
        )
        table_input = [['CE', 'Jsc (mA cm−2)', 'Voc (V)', 'FF', 'PCE'], ['Pt', '11.11', '22.22', '33.33', '44.44']]
        input_table = Table(caption=Caption(''), table_data=table_input)
        doc = Document(text_input, input_table)
        doc.add_models([PhotovoltaicCell, CommonSentenceDye])

        table_records = get_table_records(doc)
        pv_records = [PhotovoltaicRecord(record, table) for record, table in table_records]
        pv_records = add_dye_information(pv_records, doc)

        dye_record = pv_records[0].dye['Dye']
        self.assertEqual(dye_record[0], {'contextual': 'document', 'raw_value': 'N719'})



