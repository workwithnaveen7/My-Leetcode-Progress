# Last updated: 5/8/2025, 11:04:51 PM
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res=""
        stack=[]
        n=len(pattern)
        for i in range(1, n + 2): 
            if i ==n+1 or pattern[i-1]=='I':
                res+=str(i)
                while stack:
                    res += stack.pop()
            else:
                stack.append(str(i))
        return res