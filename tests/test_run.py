"""
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import unittest

from dsc_db.model import PhotovoltaicRecord
from dsc_db.run import add_dye_information, add_contextual_dye_from_document_by_multiplicity, add_distributor_info

from chemdataextractor import Document
from chemdataextractor.model import Compound
from chemdataextractor.model.pv_model import PhotovoltaicCell, SentenceDye, CommonSentenceDye
from chemdataextractor.doc import Table, Caption, Paragraph, Heading


class TestRun(unittest.TestCase):

    def test_dye_candidate_caption_substitution(self):
        """ Test the case where dye is specified in the caption"""
        table_input = [['CE',	'Jsc (mA cm−2)', 'Voc (V)', 'FF', 'PCE'], ['Pt', '11.11', '22.22', '33.33', '44.44']]
        input_table = Table(caption=Caption('Photovoltaic parameters for cells with the sensitizer N719.'), table_data=table_input)
        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        doc = Document('Null', input_table)
        doc.add_models([PhotovoltaicCell, Compound, SentenceDye, CommonSentenceDye])
        pv_records = [PhotovoltaicRecord(input, input_table)]
        pv_records = add_dye_information(pv_records, doc)
        self.assertEqual(pv_records[0].dye, {'Dye': [{'contextual': 'table_caption', 'raw_value': 'N719'}]})

    def test_dye_candidate_caption_substitution_common_sentence_dye(self):
        """Test the case where the caption contains multiple dye candidates, but one is a common dye and the other is not."""
        table_input = [['CE',	'Jsc (mA cm−2)', 'Voc (V)', 'FF', 'PCE'], ['Pt', '11.11', '22.22', '33.33', '44.44']]
        input_table = Table(caption=Caption('Photovoltaic parameters for cells with the sensitizer N719. The dye X23 was also mentioned, but this dye is not a common sentence dye.'), table_data=table_input)
        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        doc = Document('Null', input_table)
        doc.add_models([PhotovoltaicCell, Compound, SentenceDye, CommonSentenceDye])
        pv_records = [PhotovoltaicRecord(input, input_table)]
        pv_records = add_dye_information(pv_records, doc)
        self.assertEqual(pv_records[0].dye, {'Dye': [{'contextual': 'table_caption', 'raw_value': 'N719'}]})

    def test_dye_candidate_caption_substitution_multiplicity_sentence_dye(self):
        """Test the case where the caption contains multiple dye candidates, all of which are not common sentence dyes."""
        table_input = [['CE',	'Jsc (mA cm−2)', 'Voc (V)', 'FF', 'PCE'], ['Pt', '11.11', '22.22', '33.33', '44.44']]
        input_table = Table(caption=Caption('Photovoltaic parameters for cells with the sensitizer X24. The dye X23 was also mentioned. But the main dye was X24.'), table_data=table_input)
        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        doc = Document('Null', input_table)
        doc.add_models([PhotovoltaicCell, Compound, SentenceDye, CommonSentenceDye])
        pv_records = [PhotovoltaicRecord(input, input_table)]
        pv_records = add_dye_information(pv_records, doc)
        self.assertEqual(pv_records[0].dye, {'Dye': [{'contextual': 'table_caption_permissive', 'raw_value': 'X24'}]})


    def test_dye_candidate_document_substitution(self):
        """ Test the case where dye is specified in the document"""
        table_input = [['CE',	'Jsc (mA cm−2)', 'Voc (V)', 'FF', 'PCE'], ['Pt', '11.11', '22.22', '33.33', '44.44']]
        table = Table(caption=Caption('Null'), table_data=table_input)#, models=[PhotovoltaicCell])
        input_doc = Document(Paragraph('This is a test document. It says a few cool things. It also defines the dye, X23'), table)
        input_doc.add_models([PhotovoltaicCell, Compound, SentenceDye, CommonSentenceDye])
        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        pv_records = [PhotovoltaicRecord(input, table)]
        pv_records = add_dye_information(pv_records, input_doc)
        self.assertEqual({'Dye': [{'contextual': 'document_permissive', 'raw_value': 'X23'}]}, pv_records[0].dye)

    def test_dye_candidate_document_substitution_with_compound_substitution(self):
        table_input = [['CE',	'Jsc (mA cm−2)', 'Voc (V)', 'FF', 'PCE'], ['Pt', '11.11', '22.22', '33.33', '44.44']]
        table = Table(caption=Caption('Null'), table_data=table_input)
        para = Paragraph("Organic sensitizer of 3-{6-{4-[bis(2′,4′-dihexyloxybiphenyl-4-yl)amino-]phenyl}-4,4-dihexyl-cyclopenta-[2,1-b:3,4-b']dithiophene-2-yl}-2-cyanoacrylic acid (Y123) was purchased from Dyenamo and used without purification.")
        input_doc = Document(para, table)

        input_doc.add_models([PhotovoltaicCell, Compound, SentenceDye, CommonSentenceDye])
        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        expected = {'Dye': [{'raw_value': 'Y123', 'contextual': 'document',
                    'compound': {'names': ["3-{6-{4-[bis(2′,4′-dihexyloxybiphenyl-4-yl)amino-]phenyl}-4,4-dihexyl-cyclopenta-[2,1-b:3,4-b']dithiophene-2-yl}-2-cyanoacrylic acid"], 'labels': ['Y123']}}]}

        pv_records = [PhotovoltaicRecord(input, Table(caption=Caption('Null')))]
        pv_records = add_dye_information(pv_records, input_doc)

        doc_records = [record.serialize() for record in input_doc.records]
        compound_records = [record['Compound'] for record in doc_records if 'Compound' in record.keys()]
        for pv_record in pv_records:
            if pv_record.dye is not None:
                pv_record._substitute_compound('dye', 'Dye', compound_records)

        self.assertEqual(pv_records[0].dye, expected)

    def test_dye_candidate_document_substitution_with_abbreviation_substitution(self):
        input_table = Table(caption=Caption('Photovoltaic parameters for cells with the sensitizer N719.'))
        input_para = Paragraph('Here is a definition: N719 = not-my-real-name 719 ')

        input_doc = Document(input_para, input_table)
        input_doc.add_models([PhotovoltaicCell, Compound, SentenceDye, CommonSentenceDye])

        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        expected = {'Dye': [   {   'abbreviations': [['not-my-real-name', '719']],
                              'contextual': 'table_caption',
                              'raw_value': 'N719'}]}

        pv_records = [PhotovoltaicRecord(input, input_table)]
        pv_records = add_dye_information(pv_records, input_doc)

        for pv_record in pv_records:
            if pv_record.dye is not None:
                pv_record._substitute_definitions('dye', 'Dye', input_doc)

        self.assertEqual(pv_records[0].dye, expected)

    def test_dye_candidate_document_substitution_non_permissive(self):
        input_table = Table(caption=Caption(''))
        input_para = Paragraph('Photovoltaic parameters for cells with the sensitizer N719.')
        input_doc = Document(input_para, input_table)
        input_doc.add_models([PhotovoltaicCell, Compound, SentenceDye, CommonSentenceDye])

        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        expected = {'Dye': [{'contextual': 'document',
                              'raw_value': 'N719'}]
                    }

        pv_records = [PhotovoltaicRecord(input, input_table)]
        pv_records = add_dye_information(pv_records, input_doc)

        self.assertEqual(pv_records[0].dye, expected)

    def do_multiplicity_testing(self, doc):

        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        doc.add_models([PhotovoltaicCell, CommonSentenceDye])
        pv_records = [PhotovoltaicRecord(pv_input, Table(Caption('')))]
        pv_records, _ = add_contextual_dye_from_document_by_multiplicity(pv_records, doc.elements)
        for pv_record in pv_records:
            print(pv_record.serialize())
        return pv_records

    def test_dye_contextual_substitution_by_multiplicity(self):

        doc = Document(Heading('Introduction'), Paragraph('This is the intro.'),
                       Heading('Experimental'), Paragraph('This is the body of text. We used the dye N719.'),
                       Heading('Results and Discussion'), Paragraph('The results.'))

        expected = {'Dye': [{'contextual': 'document', 'raw_value': 'N719'}]}
        most_common_dyes = self.do_multiplicity_testing(doc)
        self.assertEqual(most_common_dyes[0].serialize()['dye'], expected)


    def test_dye_contextual_substitution_by_multiplicity_multiple_dyes_mentioned(self):
        doc = Document(Heading('Introduction'), Paragraph('This is the introduction.'),
                       Heading('Experimental'), Paragraph('This is the body of text. We used the dye N719. We also mention the dye D45. However, N719 is the dye used in this experiment.'),
                       Heading('Conclusions'), Paragraph('The results.'))

        expected = {'Dye': [{'contextual': 'document', 'raw_value': 'N719'}]}
        most_common_dyes = self.do_multiplicity_testing(doc)
        self.assertEqual(most_common_dyes[0].serialize()['dye'], expected)

    def test_dye_contextual_substitution_by_multiplicity_equal_mentions(self):
        """ This test checks that for cases where the most mentioned dye are equal, no dye is added."""
        doc = Document(Heading('Introduction'), Paragraph('This is the introduction.'),
                       Heading('Experimental'), Paragraph('This is the body of text. We used the dye N719. We also mention the dye D45.'
                                                          ' But how can we be sure which dye is right when N719 is mentioned twice? And dye D45 is mentioned twice too?'),
                       Heading('Conclusions'), Paragraph('The results.'))

        expected = {'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc', 'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}}
        most_common_dyes = self.do_multiplicity_testing(doc)
        print(most_common_dyes[0].serialize(), expected)

    def test_add_distributor_info(self):

        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'dye': {'Dye': [{'contextual': 'document', 'raw_value': 'N719'}]}
        }
        expected = {'Dye': [{'contextual': 'document', 'labels': ['DN-FR03',
                     'N719',
                     'N-719',
                     'black dye',
                     'N719 black dye',
                     '1-Butanaminium, N,N,N-tributyl-, hydrogen '
                     '(OC-6-32)-[[2,2´:6´,2´´-terpyridine]-4,4´,4´´-tricarboxylato(3-)-κN1,κN1´,κN1´´]tris(thiocyanato-κN)ruthenate(4-) '
                     '(2:2:1)',
                     'Di-tetrabutylammonium '
                     'cis-bis(isothiocyanato)bis(2,2′-bipyridyl-4,4′-dicarboxylato)ruthenium(II)',
                     'Ruthenium(2+) N,N,N-tributyl-1-butanaminium '
                     "4'-carboxy-2,2'-bipyridine-4-carboxylate "
                     '(thioxomethylene)azanide (1:2:2:2)',
                     "Ruthenium(2+)-N,N,N-tributyl-1-butanaminium-4'-carboxy-2,2'-bipyridin-4-carboxylat-(thioxomethylen)azanid "
                     '(1:2:2:2)',
                     'Ruthenizer 535-bisTBA',
                     'cis-diisothiocyanato-bis(2,2’-bipyridyl-4,4’-dicarboxylato) '
                     'ruthenium(II) bis(tetrabutylammonium)'],
          'name': '1-Butanaminium, N,N,N-tributyl-, hydrogen '
                  '(OC-6-32)-[[2,2´:6´,2´´-terpyridine]-4,4´,4´´-tricarboxylato(3-)-κN1,κN1´,κN1´´]tris(thiocyanato-κN)ruthenate(4-) '
                  '(2:2:1)',
          'raw_value': 'N719',
          'smiles': '[Ru++].CCCC[N+](CCCC)(CCCC)CCCC.CCCC[N+](CCCC)(CCCC)CCCC.OC(=O)c1ccnc(c1)c2cc(ccn2)C([O-])=O.OC(=O)c3ccnc(c3)c4cc(ccn4)C([O-])=O.[N-]=C=S.[N-]=C=S'}]}
        pv_records = [PhotovoltaicRecord(pv_input, Table(Caption('')))]
        pv_records = add_distributor_info(pv_records)
        self.assertEqual(expected, pv_records[0].dye)

    def test_result_removed_when_no_voc_jsc_ff_and_pce(self):

        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}},
            'dye': {'Dye': [{'contextual': 'document', 'raw_value': 'N719'}]}
        }

        expected = {}
        pv_records = [PhotovoltaicRecord(pv_input, Table(Caption('')))]



