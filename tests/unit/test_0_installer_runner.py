import pytest
from modules import sentence_smash


def describe_smash():
    def should_error_when_not_list():
        """🧪 should give an error when the input is not a list"""
        with pytest.raises(ValueError, match="❗️ Input should be a list"):
            sentence_smash.smash("blah")

    def should_return_one_character():
        """🧪 should return t for an input only containing t"""
        assert sentence_smash.smash(["t"]) == "t"

    def should_return_the_word_bob():
        """🧪 should return bob for an input only containing bob"""
        assert sentence_smash.smash(["bob"]) == "bob"
        assert sentence_smash.smash(["t"]) == "t"

    def should_return_the_word_cat():
        """🧪 should return cat for an input only containing cat"""
        assert sentence_smash.smash(["cat"]) == "cat"
