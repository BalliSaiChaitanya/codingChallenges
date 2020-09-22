#O(n) time | O(n) space
def CeasarCipher(string, key):
    newLetters = []
    newKey = key % 26
    for lttr in string:
        newLetters.append(getNewLetter(lttr,newKey))
    return "".join(lttr)

def getNewLetter(letter,key):
    newLetter= ord(letter) + key
    return chr(newLetter) if newLetter <= 122 else chr(96+ newLetter %122)


#O(n) time | O(n) space
def CeasarCipher2(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for lttr in string:
        newLetters.append(getNewLetter2(lttr,newKey,alphabet))
    return "".join(lttr)

def getNewLetter2(letter,key,alphabet):
    newLetterCode= alphabet.index(letter) + key
    return alphabet[newLetterCode] if newLetterCode <= 25 else alphabet[-1+ newLetterCode %25]