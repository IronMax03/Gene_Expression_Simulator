from typing import List

def Find_DNA_Subsequences(templateStrand: str, PromoterLst: List[str] = ["TATAAT", "TTGACA"], Terminator: str = "TTTTT") -> List[List[str]]:
    output  = []
    startIndexs = []
    end = -1

    for i in range(len(templateStrand)):
        for promoter in PromoterLst:
            if templateStrand[i:i + len(promoter)] == promoter:
                startIndexs.append(i + len(promoter))
                continue

        if Terminator == templateStrand[i:i + len(Terminator)]:
            end = i
            break

    # Error Handling
    if end == -1:
        raise Exception("[def Find_DNA_Subsequences(templateStrand: str):] No terminator found in templateStrand")
    if len(startIndexs) == 0:
        raise Exception("[def Find_DNA_Subsequences(templateStrand: str):] No promotor found in templateStrand")


    for start in startIndexs:
        output.append(templateStrand[start:end])
    
    return output

def DNA_Subsequence_To_mRNA(dnaSubsequence: str) -> str:

    DNA_RNA_maping = {
    'A' : 'U',
    'T' : 'A',
    'C' : 'G',
    'G' : 'C'
    }

    RNA_Sequence = ""

    for b in dnaSubsequence:
        if b not in ['A', 'T', 'C', 'G']:
            raise Exception("[def DNA_Subsequence_To_mRNA(dnaSubsequence: str):] Dna strand formating error.")

        RNA_Sequence = RNA_Sequence + DNA_RNA_maping[b]


    return RNA_Sequence