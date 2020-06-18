"""
classify.py

Classify papers by subject
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""

from chemdataextractor.doc import Document, Title
from chemdataextractor.reader import RscHtmlReader, ElsevierXmlReader

from dsc_db.data import psc_indicators, qdsc_indicators, dsc_indicators, token_tuples_to_merge

classifiers = [
    ('psc', psc_indicators),
    ('qdsc', qdsc_indicators),
    ('dsc', dsc_indicators)
]

hypens = [
    '-',
    '‐',
    '‑',
    '⁃',
    '‒',
    '–',
    '—',
    '―',
    '−',
    '－'
]


def classify_document(doc):
    """ Takes a paper about a 3rd-gen solar cell and classifies accordingly"""

    # Getting the title
    title = doc.titles[0]
    print('Title is: %s' % title)

    result = get_most_frequent(title)

    if not result:
        # Getting the abstract where title failed
        elements = doc.elements
        abstract = None

        # First, search for a heading that is called 'abstract', and take the following paragraph
        # This form is used in Elsevier articles
        for i, el in enumerate(elements):
            if el.__class__.__name__ == 'Heading' and el.text.lower() == 'abstract':
                # Search for the next paragraph if abstract is found
                j = i+1
                for para_el in elements[j:]:
                    if para_el.__class__.__name__ == 'Paragraph':
                        abstract = para_el
                        break

                break

        # If the abstract was not found, assuming the article is RSC.
        # For these cases, abstract is the first element before the first heading.
        if not abstract:
            first_heading = doc.headings[0]
            elements = doc.elements
            abstract = None
            # Abstract immediately proceeds the first heading (introduc   tion)
            for i, el in enumerate(elements):
                if el == first_heading and i != 0:
                    abstract = elements[i-1]

        print('Abstract is: %s' % abstract)
        result = get_most_frequent(abstract)

    if not result:
        result = 'psc'

    return result


def get_most_frequent(elem):
    """ Determines the most frequent type"""

    outputs = []

    sentences = elem.sentences
    all_tokens = [token.text.lower() for sentence in sentences for token in sentence.tokens]

    # Remove tokens that are hyphens
    filtered_tokens = [token for token in all_tokens if token not in hypens]

    # Create a list of tuples containing adjacent tokens:
    paired_tokens = list(zip(filtered_tokens, filtered_tokens[1:] + filtered_tokens[:1]))[:-1]

    # Count the occurence of each document classifier
    for _, indicator in classifiers:

        result = count_occurances(filtered_tokens, paired_tokens, indicator)
        outputs.append(result)

    if not outputs:
        return None

    max_value = max(outputs)
    if outputs.count(max_value) == 1:
        for i, output in enumerate(outputs):
            if output == max_value:
                most_frequent_classifier = classifiers[i][0]
                return most_frequent_classifier
    else:
        return None


def merge_text(all_tokens):
    """Merge tokens together that are indicators"""

    updated_tokens = []
    for i, token in enumerate(all_tokens):
        for key in token_tuples_to_merge.keys():
            if key == token and all_tokens[i+1] == token_tuples_to_merge[key]:
                updated_tokens.append('%s %s' % (token, token_tuples_to_merge[key]))


def count_occurances(filtered_tokens, paired_tokens, indicator):
    """ Counts the occurances of an indicator"""

    # Update elems to include indicators that are more than one token long
    specific_tuples_to_merge = [(first, second) for first, second in token_tuples_to_merge if
                                (first + ' ' + second) in indicator]

    # Check the token is an indicator
    elems = [token for token in filtered_tokens if token in indicator]

    elems_of_two_tokens = [token_tup for token_tup in paired_tokens if token_tup in specific_tuples_to_merge]

    return len(elems) + len(elems_of_two_tokens)




if __name__ == '__main__':
    path = '/home/edward/pv/webscraping/rsc/articles/dye%20sensitized%20solar%20cell/C5RA10148D.html' # PSC
    elsevier_path = '/home/edward/pv/webscraping/elsevier/articles/dye%20sensitized%20solar%20cell_250220/10.1016:j.tsf.2015.08.006.xml'
    document = Document.from_file(elsevier_path, readers=[ElsevierXmlReader(), RscHtmlReader()])

    # Altering the doc title to check the abstract logic works...
    # document.titles[0] = Title('nothing to see here.')

    classification = classify_document(document)
    print('Document %s classified as %s' % (path, classification))







