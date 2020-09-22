def bubbleSort(nums):
        srt=False
        temp=0
        while srt!=True:
            srt=True
            for i in range(len(nums)-1):
                if nums[i] > nums [i+1]:
                    temp=nums[i]
                    nums[i]=nums[i+1]
                    nums[i+1]=temp
                    srt=False
        return nums
                    