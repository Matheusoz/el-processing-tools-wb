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
    '''This function generates a valid phrase from a