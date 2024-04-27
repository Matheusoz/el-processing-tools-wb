from wb_cleaning.translate import translation as tr


class TestTranslation:
    def test_translate_en(self):
        txt = "pobreza"
        expected = "poverty"

        result = tr.translate(txt, src="auto", dest="en")
        returns = result["translated"]

        assert expected == returns

    def test_translate_fr(self):
        txt = "refugee"
        expected = "réfugié"

        result = tr.translate(txt, src="auto", dest="fr")
        returns = result["translated"]

        assert expected == returns

    def test_translate_shell_en(self):
        txt = "pobreza"
        expected = "poverty"

        result = tr.translate_shell(txt, src="auto", dest="en")
        returns = result["translated"]

        assert expected == returns

    def test_translat