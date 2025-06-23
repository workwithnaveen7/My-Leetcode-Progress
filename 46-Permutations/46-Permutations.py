# Last updated: 6/23/2025, 9:39:00 AM
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))
        
        