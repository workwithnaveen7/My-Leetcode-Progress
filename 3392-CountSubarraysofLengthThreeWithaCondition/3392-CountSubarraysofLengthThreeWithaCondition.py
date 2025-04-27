# Last updated: 4/27/2025, 10:06:43 PM
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        for i in range(n-2):
            left=nums[i]
            right=nums[i+2]
            mid=nums[i+1]
            if left+right==mid/2:
                count+=1
        return count
