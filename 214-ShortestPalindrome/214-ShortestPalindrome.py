# Last updated: 6/24/2025, 10:14:38 AM
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        for i in range(len(s), 0, -1):
            if s[:i] == s[:i][::-1]:
                suffix = s[i:]
                return suffix[::-1] + s
        return s[::-1] + s  # fallback (shouldn't happen)
