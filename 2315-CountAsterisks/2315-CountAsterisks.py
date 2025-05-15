# Last updated: 5/15/2025, 10:43:27 PM
class Solution:
    def countAsterisks(self, s: str) -> int:
        flag = True
        res = 0
        for i in s:
            if(i == "|"):
                flag = not flag
                continue
            if(i == "*" and flag):
                res += 1
        return res

        