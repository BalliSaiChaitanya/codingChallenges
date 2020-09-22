def selectionSort(array):
    ptr=0
    while ptr < len(array)-1:
        small=ptr
        for i in range(ptr+1,len(array)):
            if array[i] < array[small]:
                small=i
        array[small],array[ptr]=array[ptr],array[small]
        ptr += 1
