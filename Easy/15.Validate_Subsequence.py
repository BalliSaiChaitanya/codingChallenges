def ValidateSubsequence(array, sequence):
    arrIdx=0
    seqIdx=0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if sequence[seqIdx]==array[arrIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)