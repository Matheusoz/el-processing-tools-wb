from collections import Counter

import pandas as pd
from flashtext import KeywordProcessor
import inflect
from wb_cleaning.dir_manager import get_data_dir
from wb_cleaning.translate import translation

ACCENTED_CHARS = set(
 