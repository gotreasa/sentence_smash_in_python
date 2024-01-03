import pytest
from modules import sentence_smash


def describe_smash():
    def should_error_when_not_list():
        """🧪 should give an error when the input is not a list"""
        with pytest.raises(ValueError, match="❗️ Input should be a list"):
            sentence_smash.smash("blah")

    def should_error_when_not_list():
        """🧪 should return t for an input only containing t"""
        assert sentence_smash.smash(["t"]) == "t"

    def should_error_when_not_list():
        """🧪 should return bob for an input only containing bob"""
        assert sentence_smash.smash(["bob"]) == "bob"
