# Last updated: 6/22/2025, 10:54:10 PM
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        final=[]
        if len(s)%k!=0:
            s+=fill*(k-len(s)%k)
        for i in range(0,len(s),k):
            final.append(s[i:i+k])
        return final