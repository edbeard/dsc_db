"""
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

import unittest

from dsc_db.classify import classify_document, get_most_frequent

from chemdataextractor.doc import Document, Title, Paragraph, Heading


class TestClassification(unittest.TestCase):

    def test_classification_from_title(self):

        title = Title('Novel implication of a perovskite solar cell with a different chemical structure.')
        doc = Document(title)
        classification = classify_document(doc)
        self.assertEqual(classification, 'psc')

    def test_classification_from_title_by_multiplicity(self):

        title = Title('A catchy title about Perovskite solar cells (PSCs) and how they compare to quantum dot solar cells (QDSCs), with particular emphaisis on QDSCs.')
        doc = Document(title)
        classification = classify_document(doc)
        self.assertEqual(classification, 'qdsc')

    def test_classification_from_title_spiro_ometad(self):

        title = Title('Novel implication of a solar cell using the Spiro-OMeTAD hole transporter.')
        doc = Document(title)
        classification = classify_document(doc)
        self.assertEqual(classification, 'psc')

    def test_classification_of_dsc_when_explictly_mentioned_title(self):

        title = Title('Cosensitization of N719 and novel dyes in dye sensitized solar cells.')
        classification = get_most_frequent(title)
        self.assertEqual(classification, 'dsc')

    def test_classification_defaults_to_dsc(self):
        title = Title('Observing the latest developments in D S Cs).')
        abstract = Paragraph('This is an abstract describing that describes the specific experiment but doesn\'t explicitly'
                             ' mention the kind of solar cell.')
        first_heading = Heading('1. Intro')
        doc = Document(title, abstract, first_heading)
        classification = classify_document(doc)
        self.assertEqual(classification, 'dsc')

    def test_classification_from_abstract_rsc(self):

        title = Title('This is a dummy title that reveals zilch about the paper.')
        abstract = Paragraph('This abstract is recognised by its location before the first heading. It describes the'
                          'review a quantum dot solar cells.')
        first_heading = Heading('1. Intro')
        doc = Document(title, abstract, first_heading)
        classification = classify_document(doc)
        self.assertEqual(classification, 'qdsc')

    def test_classification_from_abstract_elsevier(self):

        title = Title('Nothing in this title.')
        abstract_heading = Heading('Abstract')
        abstract_para = Paragraph('Dye-sensitized solar cell (DSC) consists of a TiO2 nano film of the photo electrode, dye molecules on the surface of the TiO2 film, an electrolyte layer and a counter electrode. Among these, the nano porous TiO2 film plays an important role as the photo electrode in DSC because it adsorbs a large number of the dye molecules which provide electrons. Therefore, the condition of the TiO2 film affects the cell performance such as current density (Jsc), open circuit voltage (Voc) and fill factor (FF). The thickness of TiO2 film is one of these conditions. Its variation influences on the internal impedances of DSC related to the electron transport. In this study, we analyzed the characteristics of DSC with the different thicknesses of TiO2 film by using electrochemical impedance spectroscopy (EIS) in details. As a result, it was demonstrated that the variation of the TiO2 thickness has an effect on the electron transport in the DSC. Finally, the TiO2 thickness is optimized for the best performance of DSC.')
        doc = Document(title, abstract_heading, abstract_para)
        classification = classify_document(doc)
        self.assertEqual(classification, 'dsc')

