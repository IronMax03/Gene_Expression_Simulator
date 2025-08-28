from Toolkit import *
import pytest
import yaml
with open('scr/tests.yaml', 'r') as file: 
    testsCases = yaml.safe_load(file)

@pytest.mark.parametrize("dnaSubsequence, expected", testsCases["DNA_Subsequence_To_mRNA"])
def test_DNA_Subsequence_To_mRNA(dnaSubsequence: str, expected: str) -> None:
    if expected == "-1":
        try:
            DNA_Subsequence_To_mRNA(dnaSubsequence)
        except Exception:
            return
        else:
            raise Exception("Uncached error")
        
    else:
        assert(DNA_Subsequence_To_mRNA(dnaSubsequence) == expected)

