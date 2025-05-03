# Last updated: 5/3/2025, 11:36:45 PM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums
