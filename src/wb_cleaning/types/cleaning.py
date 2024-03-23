'''
This module contains the type definitions for the configuration parameters
of the cleaning pipeline.

This typed data structure will be used in the implementation of the API using
FastAPI.
'''

import enum
import json
from typing import List, Any
from pydantic import BaseModel, Field, validator
from wb_cleaning.utils.scripts import generate_model_hash


class SpaCyPOSTag(str, enum.Enum):
    '''Enum of SpaCy part-of-speech tags.
    '''
    # SpaCy pos tags
    adjective = "ADJ"
    adposition = "ADP"
    adverb = "ADV"
    auxiliary = "AUX"
    conjunction = "CONJ"
    coordinating_conjunction = "CCONJ"
    determiner = "DET"
    interjection = "INTJ"
    noun = "NOUN"
    numeral = "NUM"
    particle = "PART"
    pronoun = "PRON"
    proper_noun = "PROPN"
    punctuation = "PUNCT"
    subordinating_conjunction = "SCONJ"
    symbol = "SYM"
    verb = "VERB"
    other = "X"
    space = "SPACE"

    class Config:
        use_enum_values = True


class Entity(str, enum.Enum):
    '''Enum of SpaCy entities.
    '''
    cardinal = "CARDINAL"           # Numerals that do not fall under another type.
    time = "TIME"                   # Times smaller than a day.
    percent = "PERCENT"             # Percentage, including ”%“.
    money = "MONEY"                 # Monetary values, including unit.
    date = "DATE"                   # Absolute or relative dates or periods.
    quantity = "QUANTITY"           # Measurements, as of weight or distance.
    ordinal = "ORDINAL"             # “first”, “second”, etc.
    language = "LANGUAGE"           # Any named langua