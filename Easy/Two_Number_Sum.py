class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap={}
        for i in range(0,len(nums)):
            diff=target-nums[i]
            if diff in hMap:
                return [hMap[diff],i]
            hMap[nums[i]]=i
        return
