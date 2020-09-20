#Recursive 
#Average: time O(n) | space O(n) 

def branchSums(root):
    sums=[]
    bsHelper(root,0,sums)
    return sums

def bsHelper(node,runningSum,sums):
    if node is None:
        return
    newRunningSum=runningSum+node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
    bsHelper(node.left,runningSum,sums)
    bsHelper(node.right,runningSum,sums)    
