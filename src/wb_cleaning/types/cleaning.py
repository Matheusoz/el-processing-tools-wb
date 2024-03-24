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
    language = "LANGUAGE"           # Any named language.
    law = "LAW"                     # Named documents made into laws.
    work_of_art = "WORK_OF_ART"     # Titles of books, songs, etc.

    # Named hurricanes, battles, wars, sports events, etc.
    event = "EVENT"
    # Objects, vehicles, foods, etc. (Not services.)
    product = "PRODUCT"
    # Non-GPE locations, mountain ranges, bodies of water.
    loc = "LOC"
    gpe = "GPE"                     # Countries, cities, states.
    org = "ORG"                     # Companies, agencies, institutions, etc.
    # Buildings, airports, highways, bridges, etc.
    fac = "FAC"
    # Nationalities or religious or political groups.
    norp = "NORP"
    person = "PERSON"               # People, including fictional.

    class Config:
        use_enum_values = True


class LanguageFilter(BaseModel):
    """Data type for language detection.
    """
    lang: str = Field(
        ...,
        description="Language code as defined in enchant library.")
    score: float = Field(
        ...,
        description="Threshold score for a detected language to be considered as significant."
    )

    def __gt__(self, other):
        # Add this so that we could sort this class later.
        return self.lang > other.lang

    # def __eq__(self, other):
    #     return self.lang == other.lang

    def __lt__(self, other):
        # Add this so that we could sort this class later.
        return self.lang < other.lang


class CleanerFlags(BaseModel):
    """Container of flags that control the
    behavior of the cleaning pipeline.
    """
    correct_misspelling: bool = True
    exclude_entity_types: bool = True
    expand_acronyms: bool = True
    filter_stopwords: bool = True
    filter_language: bool = True
    fix_fragmented_tokens: bool = True
    include_pos_tags: bool = True
    tag_whitelisted_entities: bool = True


class CleanerParams(BaseModel):
    '''Definition of parameters for the cleaner pipeline.
    '''
    entities: List[Entity] = Field(
        .