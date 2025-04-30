# Last updated: 4/30/2025, 11:03:02 PM
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            if len(str(num))%2==0:
                count+=1

        return count