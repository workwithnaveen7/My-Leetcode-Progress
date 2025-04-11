# Last updated: 4/11/2025, 6:05:48 PM
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count=0
        mis=1
        i=0
        while mis<=n:
            if i < len(nums) and nums[i]<=mis:
                mis+=nums[i]
                i+=1
            else:
                mis+=mis
                count+=1
        return count    