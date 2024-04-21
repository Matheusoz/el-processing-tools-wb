from wb_nlp import dir_manager
from wb_cleaning.extraction import country_extractor as ce


class TestCountryExtractor:
    def test_get_normalized_country_group_name(self):
        code = "ASEAN+COUNTRIES_DATA"
        expected = [
            code,
            "asean+countries_data",
            "ASEAN COUNTRIES_DATA",
            "ASEAN+COUN