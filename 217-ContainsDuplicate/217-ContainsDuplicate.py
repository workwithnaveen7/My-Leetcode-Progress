# Last updated: 5/23/2025, 1:29:27 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False