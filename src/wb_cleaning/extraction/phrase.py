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