# O(n) time | | O(1) space 
def threeLargestNumbers(array):
    largest=[None,None,None]
    for num in array:
        updateLargtest(largest,num)
    return largest

def updateLargtest(largest,num):
    if largest[2] is None or num > largest[2]:
        shiftUpdate(largest,num,2)
    elif largest[1] is None or num > largest[1]:
        shiftUpdate(largest,num,1)
    elif largest [0] is None or num > largest[0]:
        shiftUpdate(largest,num,0)
    return largest

def shiftUpdate(largest,num,idx):
    for i in range(idx+1):
        if i==idx:
            largest[i]=num
        else:
            largest[i]=largest[i+1]
