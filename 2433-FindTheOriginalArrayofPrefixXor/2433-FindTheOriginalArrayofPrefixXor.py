# Last updated: 4/21/2025, 12:02:56 AM
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans=[pref[0]]
        for i in range(1,len(pref)):
            res=pref[i]^pref[i-1]
            ans.append(res)

        return ans
            