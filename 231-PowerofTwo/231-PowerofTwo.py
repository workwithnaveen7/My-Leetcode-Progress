# Last updated: 5/21/2025, 5:49:07 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n <=0:
        #     return False
        # num=0
        # while num<=n:
        #     if 2**num==n:
        #         return True
        #     num+=1
        # return False

        return n>0 and (n & (n-1)) ==0