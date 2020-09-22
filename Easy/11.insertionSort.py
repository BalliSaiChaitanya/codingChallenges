# O(n^2) time || O(1) Space
def insertionSort(array):
    for i in range(1,len(array)):
        j=i
        while j > 0 and array[j] < array[j-1]:
            swap(j,j-1,array)
            j -= 1 
    return array

 def swap(i,j,arr):
     arr[i],arr[j]=arr[j],arr[i]