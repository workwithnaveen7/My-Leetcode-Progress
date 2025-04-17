# Last updated: 4/18/2025, 12:14:17 AM
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1): 
            count=bin(i).count('1')
            ans.append(count)
        return ans