#Recursive
# O(log(n)) time | | O(log(n)) Space
def binarySearch(array,target):
    return bsHelper(array,target,0,len(array)-1)

def bsHelper(array, target, left, right):
    if left > right:
        return -1
    mid=(left+right)//2
    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return bsHelper(array, target, left, mid-1) 
    else:
        return bsHelper(array, target, mid+1, right)

# Iterative
# O(log(n)) time | | O(1)
def binarySearch(array,target,left,right):
    while left <= right:
        mid=(left+right)//2
        if array[mid] == target:
            return mid
        elif target > array[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1
