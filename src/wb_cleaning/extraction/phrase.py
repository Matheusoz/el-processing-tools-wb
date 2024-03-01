'''
This module contains methods that processes texts to extract phrases.
'''
from typing import Callable, Optional
import functools

import spacy
import nltk

from nltk import WordNetLemmatizer
from nltk.corpus import wordnet

try:
    # Test if wordnet is available else download.
    wordnet.ADJ
except LookupError:
    nltk.download("wordnet")

PHRASE_FILLERS = ['of', 'the', 'in']  # Not used if
SPACY_PHRASE_POS = ['ADJ', 'NOUN']  # , 'ADV']
NLTK_PHRASE_POS = ['JJ', 'NN']  # , 'RB']
PHRASE_SEP = '_'

NLTK_TAG_MAP = {
    'J': wordnet.ADJ,
    'N': wordnet.NOUN,
    # 'R': wordnet.ADV
}

SPACY_LIB = 'SpaCy'
NLTK_LIB = 'NLTK'

wordnet_lemmatizer = WordNetLemmatizer()


@functools.lru_cache(maxsize=1024)
def get_nltk_lemma(token, pos):
    return wordnet_lemmatizer.lemmatize(token, pos=NLTK_TAG_MAP.get(pos[0], wordnet.NOUN)).lower()


def generate_phrase(phrase_tokens: list, phrase_pos: list, library: str):
    '''This function generates a valid phrase from a list of tokens.

    Additionally, the function removes dangling PHRASE_FILLERS if present.

    library should be either SpaCy or NLTK.
    '''

    noun_form = 'NOUN' if library == 'SpaCy' else 'NN'

    valid_set = False
    for phpos in phrase_pos:
        if phpos.startswith(noun_form):
            valid_set = True
            break

    if not valid_set:
        return None

    while True and phrase_tokens:
        if not phrase_pos[-1].startswith(noun_form):
            phrase_tokens.pop(-1)
            phrase_pos.pop(-1)
        else:
            break

    sub_phrase = []
    for idx, i in enumerate(phrase_pos[::-1]):
        if not i.startswith(noun_form):
            if idx > 1:
                sub_phrase = PHRASE_SEP.join(phrase_tokens[-idx:])
            break

    phrases = [PHRASE_SEP.join(phrase_tokens)]
    if sub_phrase:
        phrases.append(sub_phrase)

    return phrases if len(phrase_tokens) > 1 else None


def get_spacy_phrases(
        doc: spacy.tokens.doc.Doc