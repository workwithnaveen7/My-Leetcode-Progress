# Last updated: 6/11/2025, 10:17:19 PM
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        for i in range(len(word)):
            if word[i]==ch:
                res=word[:i+1][::-1]+word[i+1:]
                return res


