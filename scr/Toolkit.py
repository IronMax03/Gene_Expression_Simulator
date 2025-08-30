from typing import List, Tuple
import yaml
with open('scr/config.yaml', 'r') as file: 
    config = yaml.safe_load(file)


class GeneExpressionError(Exception):
    """Base class for simulator-specific errors."""


class DNAError(GeneExpressionError):
    """Invalid or improperly formatted DNA sequences."""


class RNAError(GeneExpressionError):
    """Invalid or improperly formatted RNA sequences."""


class CapTypeError(GeneExpressionError):
    """Unsupported or unknown cap type."""


class TailError(GeneExpressionError):
    """Errors related to poly(A) tail tokens or lengths."""

def DNA_Subsequence_To_mRNA(dnaSubsequence: str) -> str:

    DNA_RNA_maping = {
    'A' : 'U',
    'T' : 'A',
    'C' : 'G',
    'G' : 'C'
    }

    RNA_Sequence = ""

    for b in dnaSubsequence:
        if b not in ['A', 'T', 'C', 'G', 'a', 't', 'c', 'g']:
            raise DNAError("[def DNA_Subsequence_To_mRNA(dnaSubsequence: str):] Dna strand formating error.")

        RNA_Sequence = RNA_Sequence + DNA_RNA_maping[b.upper()]

    return RNA_Sequence


def Find_DNA_Subsequences(templateStrand: str, PromoterLst: List[str] = ["TATAAT", "TTGACA"], Terminator: str = "TTTTT") -> List[List[str]]:
    dnaOutput  = []
    promoterOutput = []
    temp = []
    startIndexs = []

    i = 0
    while i < len(templateStrand):
        for promoter in PromoterLst:
            if templateStrand[i:i + len(promoter)] == promoter:
                startIndexs.append(i + len(promoter))
                temp.append(promoter)
                continue

        if Terminator == templateStrand[i:i + len(Terminator)]:
            for start in startIndexs:
                dnaOutput.append(templateStrand[start:i])
                promoterOutput.append(temp.pop(0))
            temp.clear()
            templateStrand = templateStrand[i + len(Terminator):]
            print(templateStrand)
            i = 0
            startIndexs = []
            continue
        i = i + 1
    
    return [dnaOutput, promoterOutput]

# Eukaryotes
def add_cap_and_tail(rna_seq:str, cap_type:int, tail_length:int) -> Tuple[str, str, str]:

    for b in rna_seq:
        if b.upper() not in ["A", "U", "G", "C"]:
            raise RNAError("RNA sequence must contain only A/C/G/U.")

    cap_key = f"cap{cap_type}" if isinstance(cap_type, int) else str(cap_type).strip().lower()
    if cap_key not in config["cap_type_to_biochemical_map"]:
        raise CapTypeError("Unknown cap type")
    return (f"5\'cap{cap_type} ", rna_seq, "A"+ str(tail_length))

# Eukaryotes
def convert_to_single_string(mature_mRNA:Tuple[str, str, str]) -> str:
    tail = ""
    if mature_mRNA[0] not in ["A", "U", "G", "C"] or isinstance(mature_mRNA[0:],int):
        raise TailError("The tail is not formated correctly")
    elif int(mature_mRNA[0:]) < 0:
        raise TailError("Tail size must be positive")
    
    for i in range(int(mature_mRNA[2][1:])):
        tail = tail + mature_mRNA[2][0]
    return f"{mature_mRNA[0]}{mature_mRNA[1]}{tail} 3\'"

# Eukaryotes
def cap_type_to_biochemical(cap_type:str) -> str:
    biochemicalMap = config["cap_type_to_biochemical_map"]

    if cap_type not in biochemicalMap:
        raise CapTypeError("Unknown cap type")
    return biochemicalMap[cap_type]
