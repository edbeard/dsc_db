"""
Classify multiple documents
"""
import os
from shutil import copy
from dsc_db.classify import classify_document
from chemdataextractor import Document

root_dir = '/home/edward/pv/extractions/input'
output_path = '/home/edward/pv/extractions/input_filtered'


if __name__ == '__main__':

    list_of_papers = [os.path.join(root_dir, paper) for paper in os.listdir(root_dir)]

    print('Begining classification...')
    for paper in list_of_papers:
        try:
            with open(paper, 'rb') as f:
                doc = Document.from_file(f)

            classification = classify_document(doc)

            # Try obtaining metadata to trigger html exception
            meta = doc.metadata
        except:
            classification = 'format_error'

        if classification == 'dsc':
            copy(paper, os.path.join(output_path, 'dsc'))
        elif classification == 'psc':
            copy(paper, os.path.join(output_path, 'psc'))
        elif classification == 'qdsc':
            copy(paper, os.path.join(output_path, 'qdsc'))
        elif classification == 'format_error':
            copy(paper, os.path.join(output_path, 'qdsc'))
        else:
            copy(paper, os.path.join(output_path, 'algorithm_failures'))

        print('paper: %s classified as: %s' % (paper, classification))

    print('Classification complete.')
