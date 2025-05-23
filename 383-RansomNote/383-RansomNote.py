# Last updated: 5/23/2025, 2:48:30 PM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count=Counter(ransomNote)
        mag_count=Counter(magazine)
        for char in ransom_count:
            if ransom_count[char]>mag_count[char]:
                return False
        return True