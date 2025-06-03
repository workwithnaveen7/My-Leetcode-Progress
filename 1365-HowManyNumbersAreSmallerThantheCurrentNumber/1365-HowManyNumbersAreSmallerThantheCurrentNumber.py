# Last updated: 6/3/2025, 9:23:57 PM
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count+=1
            ans.append(count)
        return ans