# Last updated: 4/25/2025, 11:56:26 PM
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        sum=0
        num=str(n) #"234"
        for i in num:
            prod=prod*int(i)
            sum=sum+int(i)
        return prod-sum