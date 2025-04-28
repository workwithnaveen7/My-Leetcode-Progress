# Last updated: 4/28/2025, 11:22:43 PM
class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n=len(nums)
        left=0
        curr_sum=0
        ans=0
        for right in range(n):
            curr_sum+=nums[right]
            while left <= right and curr_sum *(right-left+ 1)>= k:
                curr_sum-=nums[left]
                left+=1
            ans +=(right-left+ 1)
        
        return ans
