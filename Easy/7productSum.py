# O(n) time || O(d) space
def producctSum(array,M=1):
    sum = 0
    for i in array:
        if isinstance(i, list):
            sum += producctSum(i,M+1)
        else:
            sum += i
    return sum * M
