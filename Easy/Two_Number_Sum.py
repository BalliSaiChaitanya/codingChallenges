class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap={}
        for i,j in enumerate(nums):
            diff=target-j
            if diff in hMap:
                return [hMap[diff],i]
            hMap[j]=i
        return
