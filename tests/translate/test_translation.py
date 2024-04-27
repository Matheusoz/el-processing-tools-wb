from wb_cleaning.translate import translation as tr


class TestTranslation:
    def test_translate_en(self):
        txt = "pobreza"
        expected = "poverty"

        result = tr.translate(txt, src="auto", dest="en")
        returns = result["transla