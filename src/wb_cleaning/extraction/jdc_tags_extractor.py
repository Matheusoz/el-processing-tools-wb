from collections import Counter

import pandas as pd
from flashtext import KeywordProcessor
import inflect
from wb_cleaning.dir_manager import get_data_dir
from wb_cleaning.translate import translation

ACCENTED_CHARS = set(
    "ÂÃÄÀÁÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ")

jdc_tags_processor = KeywordProcessor()
jdc_tags_processor.set_non_word_boundaries(
    jdc_tags_processor.non_word_boundaries | ACCENTED_CHARS)

inflect_engine = inflect.engine()

# input schema
# -> tag_value
# -> tag_prototypes

# Definition of data input:
# The input to the tag extractor is an excel or csv file.
# The first column of the data must be the intended tag keyword.
# To remove ambiguity, a header with name "tag_keyword" must be present.
