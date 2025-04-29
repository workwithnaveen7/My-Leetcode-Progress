# Last updated: 4/29/2025, 11:05:24 PM
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val=max(nums)
        count=0
        left=0
        max_count=0

        for right in range(len(nums)):
            if nums[right]==max_val:
                max_count+=1
            
            while max_count>=k:
                if nums[left]==max_val:
                    max_count -=1
                left +=1
            count+=left
        return count
