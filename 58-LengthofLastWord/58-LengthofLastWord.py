# Last updated: 5/23/2025, 2:30:22 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        return len(s.split()[-1])