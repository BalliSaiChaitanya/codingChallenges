# O(n) time | | O(1) space
def isPalindrome4(string):
    left=0
    right=len(string) -1
    while left < right:
        if string[left] != string[left]:
            return -1
        left += 1
        right -=1
    return True
        
# O(n^2) time Because for string concatination ot takes addtional n time and || O(n) space
def isPalindrome1(string):
    reverseString=""
    for i in range(len(string),0,-1):
        reverseString += string[i]
    return reverseString == string

# O(n) time | | O(n) space
def isPalindrome2(string):
    reverseChars=[]
    for i in range(len(string),0,-1):
        reverseChars.append(string[i])
    return string == "".join(reverseChars)

#Recursion
# O(n) time | | O(n) space 
def isPalindrome3(string,i=0):
    i=0
    j=len(string)-i-1
    return string[i] == string[j] and isPalindrome3(string,i+1)

