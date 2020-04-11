"""
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import unittest

from dsc_db.model import PhotovoltaicRecord
from dsc_db.run import add_dye_information, add_contextual_dye_from_document_by_multiplicity, add_distributor_info, add_contextual_info, get_filtered_elements, dsc_properties

from chemdataextractor import Document
from chemdataextractor.model import Compound
from chemdataextractor.model.pv_model import PhotovoltaicCell, SentenceDye, CommonSentenceDye, SimulatedSolarLightIntensity, Substrate, Semiconductor, DyeLoading, SentenceDyeLoading
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
        filtered_elements = []
        pv_records = add_dye_information(pv_records, filtered_elements)
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
        filtered_elements = []
        pv_records = add_dye_information(pv_records, filtered_elements)
        self.assertEqual(pv_records[0].dye, {'Dye': [{'contextual': 'table_caption', 'raw_value': 'N719'}]})

    def test_dye_candidate_caption_substitution_common_sentence_dye_2(self):
        table_input = [['CE',	'Jsc (mA cm−2)', 'Voc (V)', 'FF', 'PCE'], ['Pt', '11.11', '22.22', '33.33', '44.44']]
        input_table = Table(caption=Caption('Characteristics of N719-DSCs obtained at 1000 W/m2 and with grafted photo anodes (grafted by CV in 1 mM solutions of 1).'), table_data=table_input)
        input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                       'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        doc = Document('Null', input_table)
        doc.add_models([PhotovoltaicCell, Compound, SentenceDye, CommonSentenceDye])
        pv_records = [PhotovoltaicRecord(input, input_table)]
        filtered_elements = []
        pv_records = add_dye_information(pv_records, filtered_elements)
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
        filtered_elements = []
        pv_records = add_dye_information(pv_records, filtered_elements)
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
        filtered_elements = get_filtered_elements(input_doc)
        pv_records = [PhotovoltaicRecord(input, table)]
        pv_records = add_dye_information(pv_records, filtered_elements)
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

        filtered_elements = get_filtered_elements(input_doc)

        pv_records = [PhotovoltaicRecord(input, Table(caption=Caption('Null')))]
        pv_records = add_dye_information(pv_records, filtered_elements)

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

        filtered_elements = get_filtered_elements(input_doc)

        pv_records = [PhotovoltaicRecord(input, input_table)]
        pv_records = add_dye_information(pv_records, filtered_elements)

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
        filtered_elements = get_filtered_elements(input_doc)

        pv_records = [PhotovoltaicRecord(input, input_table)]
        pv_records = add_dye_information(pv_records, filtered_elements)

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

    def do_contextual_table_caption_merging(self, caption_text, model, expected):
        caption = Caption(caption_text)
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        pv_records = [PhotovoltaicRecord(pv_input, Table(caption, models=[model]))]
        filtered_elements = []
        pv_records = add_contextual_info(pv_records, filtered_elements, dsc_properties)
        output = pv_records[0].serialize()
        self.assertEqual(output, expected)

    def do_contextual_document_merging(self, text, model, expected):
        filtered_elements = Paragraph(text)
        doc = Document(filtered_elements)
        doc.add_models([model])
        pv_input = {
            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)', 'raw_value': '756', 'specifier': 'Voc',
                                           'units': '(10^-3.0) * Volt^(1.0)', 'value': [756.0]}}
        }
        pv_records = [PhotovoltaicRecord(pv_input, Table(Caption(''), models=[model]))]
        pv_records = add_contextual_info(pv_records, doc, dsc_properties)
        output = pv_records[0].serialize()
        self.assertEqual(output, expected)

    def test_contextual_solar_irradiance_merged_from_table_caption(self):

        caption = 'Photovoltaic parameters of various SD/ERD systems measured under simulated AM 1.5G irradiance (100 mW cm−2)'
        model = SimulatedSolarLightIntensity
        expected = {'solar_simulator': {'SimulatedSolarLightIntensity': {'contextual': 'table_caption',
                                                      'raw_units': 'mWcm−2)',
                                                      'raw_value': '100',
                                                      'specifier': 'irradiance',
                                                      'spectra': 'AM 1.5G',
                                                      'units': '(10^1.0) * '
                                                               'Meter^(-2.0)  '
                                                               'Watt^(1.0)',
                                                      'value': [100.0]}},
                     'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                    'raw_value': '756',
                                                    'specifier': 'Voc',
                                                    'units': '(10^-3.0) * Volt^(1.0)',
                                                    'value': [756.0]}}}
        self.do_contextual_table_caption_merging(caption, model, expected)

    def test_contextual_solar_irradiance_merged_from_sentence(self):

        text = 'Detailed photovoltaic parameters of solar cells based on different TiO2 photoelectrodes under AM 1.5 illumination (100 mW cm−2).'
        model = SimulatedSolarLightIntensity
        expected = {'solar_simulator': {'SimulatedSolarLightIntensity': {'raw_units': 'mWcm−2)',
                                                      'raw_value': '100',
                                                      'specifier': 'illumination',
                                                      'spectra': 'AM 1.5',
                                                      'units': '(10^1.0) * '
                                                               'Meter^(-2.0)  '
                                                               'Watt^(1.0)',
                                                      'value': [100.0],
                                                        'contextual': 'document'}},
                                         'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                                        'raw_value': '756',
                                                                        'specifier': 'Voc',
                                                                        'units': '(10^-3.0) * Volt^(1.0)',
                                                                        'value': [756.0]}}}

        self.do_contextual_document_merging(text, model, expected)

    def test_contextual_substrate_merged_from_table_caption(self):
        caption = 'PV parameters where the device had some other parameter set and a substrate of FTO.'
        model = Substrate
        expected = {'substrate': {'Substrate': {'raw_value': 'FTO',
                                                'specifier': 'substrate',
                                                'contextual': 'table_caption'}},
                                         'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                                        'raw_value': '756',
                                                                        'specifier': 'Voc',
                                                                        'units': '(10^-3.0) * Volt^(1.0)',
                                                                        'value': [756.0]}}}

        self.do_contextual_table_caption_merging(caption, model, expected)

    def test_contextual_substrate_merged_from_document(self):
        text = 'The XRD patterns with the main peaks and the Miller indices of FTO substrate, FTO/TiO2 and FTO/TiO2/CdS electrodes are shown in Fig. 1 (e).'
        model = Substrate
        expected = {'substrate': {'Substrate': {'raw_value': 'FTO',
                                                      'specifier': 'substrate',
                                                'contextual': 'document'}},
                                         'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                                        'raw_value': '756',
                                                                        'specifier': 'Voc',
                                                                        'units': '(10^-3.0) * Volt^(1.0)',
                                                                        'value': [756.0]}}}
        self.do_contextual_document_merging(text, model, expected)

    def test_contextual_semiconductor_merged_from_table_caption(self):
        caption = 'Photovoltaic parameters of the DSSCs sensitized with P1, P2 and P3 with 12 μm TiO2 photoanode'
        model = Semiconductor
        expected = {'semiconductor': {'Semiconductor': {'raw_value': 'TiO2',
                                     'specifier': 'photoanode',
                                     'thickness': {'SemiconductorThickness': {'raw_units': 'μm',
                                                                              'raw_value': '12',
                                                                              'specifier': 'photoanode',
                                                                              'units': '(10^-6.0) '
                                                                                       '* '
                                                                                       'Meter^(1.0)',
                                                                              'value': [12.0]}},
                                      'contextual': 'table_caption'}},
                     'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                    'raw_value': '756',
                                                    'specifier': 'Voc',
                                                    'units': '(10^-3.0) * Volt^(1.0)',
                                                    'value': [756.0]}}}

        self.do_contextual_table_caption_merging(caption, model, expected)

    def test_contextual_semiconductor_merged_from_document(self):
        text = 'The overall power conversion efficiencies (PCEs) of DSSCs based on these dyes lay in the range 2.46–3.9% using a 12 μm thick TiO2 photoanode.'
        model = Semiconductor
        expected = {'semiconductor': {'Semiconductor': {'contextual': 'document',
                                     'raw_value': 'TiO2',
                                     'specifier': 'photoanode',
                                     'thickness': {'SemiconductorThickness': {'raw_units': 'μm',
                                                                              'raw_value': '12',
                                                                              'specifier': 'thick',
                                                                              'units': '(10^-6.0) '
                                                                                       '* '
                                                                                       'Meter^(1.0)',
                                                                              'value': [12.0]}}}},
                                     'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                                                    'raw_value': '756',
                                                                    'specifier': 'Voc',
                                                                    'units': '(10^-3.0) * Volt^(1.0)',
                                                                    'value': [756.0]}}}
        self.do_contextual_document_merging(text, model, expected)

    def test_contextual_dye_loading_merged_from_table_caption(self):

        caption = 'with a dye-loading capacity of two working electrodes: 2.601×10−7 mol cm−2'
        model = SentenceDyeLoading
        expected = {'dye_loading': {'SentenceDyeLoading': {'contextual': 'table_caption',
                                        'exponent': [-7.0],
                                        'raw_units': 'molcm−2',
                                        'raw_value': '2.601',
                                        'specifier': 'loading',
                                        'units': '(10^4.0) * Meter^(-2.0)  '
                                                 'Mol^(1.0)',
                                        'value': [2.601]}},
                            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                'raw_value': '756',
                                'specifier': 'Voc',
                                'units': '(10^-3.0) * Volt^(1.0)',
                                'value': [756.0]}}}

        self.do_contextual_table_caption_merging(caption, model, expected)

    def test_contextual_dye_loading_merged_from_document(self):
        text = 'with a dye-loading capacity of two working electrodes: 2.601×10−7 mol cm−2'
        model = SentenceDyeLoading
        expected = {'dye_loading': {'SentenceDyeLoading': {'contextual': 'document',
                                        'exponent': [-7.0],
                                        'raw_units': 'molcm−2',
                                        'raw_value': '2.601',
                                        'specifier': 'loading',
                                        'units': '(10^4.0) * Meter^(-2.0)  '
                                                 'Mol^(1.0)',
                                        'value': [2.601]}},
                            'voc': {'OpenCircuitVoltage': {'raw_units': '(mV)',
                                'raw_value': '756',
                                'specifier': 'Voc',
                                'units': '(10^-3.0) * Volt^(1.0)',
                                'value': [756.0]}}}
        self.do_contextual_document_merging(text, model, expected)

    def test_filtering_logic(self):

        pv_record1 = PhotovoltaicRecord({})
        pv_record1.voc, pv_record1.jsc, pv_record1.ff, pv_record1.pce = 'a', 'b', 'c', 'd'

        pv_records = [pv_record for pv_record in [pv_record1] if any([getattr(pv_record, 'voc', 'None'), getattr(pv_record, 'jsc', 'None'),
                                                 getattr(pv_record, 'ff', 'None'), getattr(pv_record, 'pce', 'None')])]

        self.assertEqual(pv_records[0].serialize(), {'jsc': 'b', 'voc': 'a', 'pce': 'd', 'ff': 'c'})

        pv_record2 = PhotovoltaicRecord({})
        pv_record2.voc, pv_record2.jsc, pv_record2.ff = 'a', 'b', 'c'

        pv_records = [pv_record for pv_record in [pv_record2] if any([getattr(pv_record, 'voc', 'None'), getattr(pv_record, 'jsc', 'None'),
                                                 getattr(pv_record, 'ff', 'None'), getattr(pv_record, 'pce', 'None')])]

        self.assertEqual(pv_records[0].serialize(), {'jsc': 'b', 'voc': 'a', 'ff': 'c'})

        pv_record3 = PhotovoltaicRecord({})

        pv_records = [pv_record for pv_record in [pv_record3] if any([getattr(pv_record, 'voc', 'None'), getattr(pv_record, 'jsc', 'None'),
                                                 getattr(pv_record, 'ff', 'None'), getattr(pv_record, 'pce', 'None')])]

        self.assertEqual(pv_records, [])
