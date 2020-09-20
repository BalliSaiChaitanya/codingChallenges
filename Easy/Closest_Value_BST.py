#Recursive 
#Average: time O(log(n)) space O(log(n)) 
#Worst  : time O(n)      space O(n)
def minDiff(root, K, closest=float("inf")):
    if root is None:
        return abs(k-closest)
    if abs(k-closest) > abs(k-root.data):
        closest=root.data 
    if k < root.data:
        return minDiff(root.left,k,closest)
    elif k > root.data:
        return minDiff(root.right,k,closest)
    else:
        return 0
        
#Itearative
#Average: time O(log(n)) space O(1) 
#Worst  : time O(n)      space O(1)
def minDiff(root, K, closest=float("inf")):
    currentnode=root
    while currentnode is not None:
        if abs(closest-k) > abs(k-currentnode.data):
            closest=currentnode.data
        if k > currentnode.data:
            currentnode=currentnode.right 
        elif k < currentnode.data:
            currentnode=currentnode.left
        else:
            return 0
    return abs(k-closest)

