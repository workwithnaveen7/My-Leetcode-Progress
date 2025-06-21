# Last updated: 6/21/2025, 11:21:27 PM
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnts = Counter(word)
        vals = sorted(list(cnts.values()))
        res = float('inf')
        leftdel = 0

        for i in range(len(vals)):
            if 0 < i:
                leftdel += vals[i-1]
            limit = k + vals[i]
            currdel = leftdel
            for j in range(i, len(vals)):
                currdel += max(0, vals[j] - limit)
            res = min(res, currdel)

        return res
        