
from pathlib import Path
import re
from collections import Counter

import pandas as pd
from flashtext import KeywordProcessor

from wb_cleaning.extraction.whitelist import mappings
from wb_cleaning.dir_manager import get_data_dir
from wb_cleaning.types.metadata_enums import RegionTypes

ACCENTED_CHARS = set(
    "ÂÃÄÀÁÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ")

country_code_processor = KeywordProcessor()
country_code_processor.set_non_word_boundaries(
    country_code_processor.non_word_boundaries | ACCENTED_CHARS)

country_group_processor = KeywordProcessor()
country_group_processor.set_non_word_boundaries(
    country_group_processor.non_word_boundaries | ACCENTED_CHARS)


def get_standardized_regions(iso_code="iso3c"):
    assert iso_code in ["iso2c", "iso3c", "full"]

    codelist_path = Path(get_data_dir(
        "whitelists", "countries", "codelist.xlsx"))

    standardized_regions_path = codelist_path.parent / "standardized_regions.xlsx"

    if not standardized_regions_path.exists():

        codelist = pd.read_excel(codelist_path)
        iso_region = codelist[["country.name.en", "iso2c", "iso3c", "region"]]
        standardized_regions = iso_region.dropna(
            subset=["iso2c", "region"]).set_index("iso2c")

        standardized_regions.to_excel(standardized_regions_path)
    else:
        standardized_regions = pd.read_excel(standardized_regions_path)

    if iso_code != "full":
        standardized_regions = standardized_regions.reset_index().set_index(iso_code)[
            "region"].to_dict()

    return standardized_regions


def get_normalized_country_group_name(code):
    return [
        code,
        code.lower(),
        code.replace("+", " "),
        code.replace("_", " "),
    ]


def get_country_name_from_code(code):
    name = None
    detail = iso3166_3_country_info.get(code)
    if detail:
        name = detail.get("name")

    return name


def get_country_code_from_name(name):
    return mapping.get(name, {}).get("code")


def replace_country_group_names(txt):
    return country_group_processor.replace_keywords(txt)


def replace_countries(txt):
    return country_code_processor.replace_keywords(txt)


def load_country_groups_names():
    return pd.read_excel(
        get_data_dir("whitelists", "countries", "codelist.xlsx"),
        sheet_name="groups_names", header=0, index_col=0).to_dict()["Full name"]


def get_country_counts(txt):
    txt = re.sub(r"\s+", " ", txt)
    try:
        replaced = replace_countries(txt)
    except IndexError:
        return None
    counts = Counter([i.split(DELIMITER)[-1].strip()
                     for i in replaced.split() if i.startswith(anchor_code)])
    counts = dict(counts.most_common())

    return counts


def get_country_count_details(counts):
    if counts is None:
        return None
    data = []
    total = sum(counts.values())

    for code, count in counts.items():
        detail = iso3166_3_country_info.get(code)

        if detail is None:
            detail = {}

        #   "code": "JAM",
        #   "count": 1,
        #   "name": "Jamaica",
        #   "alpha-2": "JM",
        #   "country-code": 388,
        #   "iso_3166-2": "ISO 3166-2:JM",
        #   "region": "Americas",
        #   "sub-region": "Latin America and the Caribbean",
        #   "intermediate-region": "Caribbean",