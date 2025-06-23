# Last updated: 6/23/2025, 10:14:19 AM
from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ans=list(set(permutations(nums)))
        return ans
        