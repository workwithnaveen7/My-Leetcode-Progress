# Last updated: 6/3/2025, 9:13:20 PM
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        def dividingNum(n):
            for digit in str(n):
                if digit=='0' or n%int(digit)!=0:
                    return False
            return True
        for num in range(left,right+1):
            #if dividingNum(num)==True:
            if dividingNum(num):
                ans.append(num)
        return ans