from Toolkit import *
import pytest

@pytest.mark.parametrize("dnaSubsequence, expected", [
    ("TACGAT", "AUGCUA"),
    ("AGCY", "-1"),
    ])
def test_DNA_Subsequence_To_mRNA(dnaSubsequence: str, expected: str) -> None:
    if expected == "-1":
        try:
            DNA_Subsequence_To_mRNA(dnaSubsequence)
        except Exception:
            return
        else:
            raise Exception("Missed cached error")
        
    else:
        assert(DNA_Subsequence_To_mRNA(dnaSubsequence) == expected)

