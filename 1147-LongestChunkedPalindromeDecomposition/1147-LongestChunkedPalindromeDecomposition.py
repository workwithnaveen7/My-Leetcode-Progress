# Last updated: 4/11/2025, 11:12:36 PM
class Solution:
    def longestDecomposition(self, text: str) -> int:
        res, l, r = 0, "", ""
        for i, j in zip(text, text[::-1]):
            l, r = l + i, j + r
            if l == r:
                res, l, r = res + 1, "", ""
        return res