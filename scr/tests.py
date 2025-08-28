from Toolkit import *
import pytest
import yaml
with open('scr/tests.yaml', 'r') as file: 
    testsCases = yaml.safe_load(file)

# run tests: pytest --quiet scr/tests.py

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

@pytest.mark.parametrize("expected, templateStrand", testsCases["Find_DNA_Subsequences"])
def test_Find_DNA_Subsequences(expected: List[str] , templateStrand: str, PromoterLst: List[str] = ["TATAAT", "TTGACA"], Terminator: str = "TTTTT") -> None:
    assert(Find_DNA_Subsequences(templateStrand, PromoterLst, Terminator) == expected)
