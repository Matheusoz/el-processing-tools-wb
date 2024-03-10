import pandas as pd
from wb_cleaning.extraction import whitelist


def get_countries_mapping():
    country_df = pd.read_csv(whitelist.get_country_csv(), index_col=0, he