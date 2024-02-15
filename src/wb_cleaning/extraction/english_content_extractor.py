import re
import enchant
import pandas as pd
from scipy.stats import beta


def filter_document_by_language(txt, pval=0.05, en_dict=enchant.Dict("en_US"), return_en=True, return_df=False):
    '''Remove contents of documents that are unlikely to be in English.

    This uses statistical hypothesis testing to automate the removal of tokens.

    Other formulation:
    compute overlap in distribu