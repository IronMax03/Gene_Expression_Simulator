from typing import List


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
                temp.append(promoter)##########################
                continue

        if Terminator == templateStrand[i:i + len(Terminator)]:
            for start in startIndexs:
                dnaOutput.append(templateStrand[start:i])
                promoterOutput.append(temp.pop(0))
            templateStrand = templateStrand[i + len(Terminator):]
            print(templateStrand)
            i = 0
            startIndexs = []
        i = i + 1
    
    return [dnaOutput, promoterOutput]