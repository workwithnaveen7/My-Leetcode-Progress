# Last updated: 4/11/2025, 8:28:37 PM
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for num in range(low,high+1):
            if len(str(num))%2==0:
                digits= [int(d) for d in str(num)]
                n=len(digits)
                half=n//2
                sum1=sum(digits[:half])
                sum2=sum(digits[half:])
                if sum1==sum2:
                    count+=1
        return count