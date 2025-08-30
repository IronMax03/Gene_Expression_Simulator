from Toolkit import *
import pytest
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

@pytest.mark.parametrize("expected, rna_seq, cap_type, tail_length", testsCases["add_cap_and_tail"])
def test_add_cap_and_tail(expected:str, rna_seq:str, cap_type:int, tail_length:int) -> None:
        if expected == "-1":
            try:
                add_cap_and_tail(rna_seq, cap_type, tail_length)
            except Exception:
                return
            else:
                raise Exception("Uncached error")
        else:
            assert convert_to_single_string(add_cap_and_tail(rna_seq, cap_type, tail_length)) == expected

@pytest.mark.parametrize("expected, mature_mRNA", testsCases["add_cap_and_tail"])
def test_convert_to_single_string(expected:str, mature_mRNA:(str, str, str)) -> None:
    assert convert_to_single_string(mature_mRNA)


