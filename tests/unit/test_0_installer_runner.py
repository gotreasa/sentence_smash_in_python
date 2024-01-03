import pytest
from modules import sentence_smash


def describe_smash():
    def should_error_when_not_list(capsys):
        """🧪 should give an error when the input is not a list"""
        with pytest.raises(ValueError, match="❗️ Input should be a list"):
            sentence_smash.smash("blah")
