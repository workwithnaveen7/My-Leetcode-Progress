# Last updated: 6/19/2025, 11:07:24 PM
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            sum = 0
            while num:
                sum += num%10
                num = num//10
                
            num = sum

        return num       