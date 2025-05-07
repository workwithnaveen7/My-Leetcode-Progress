# Last updated: 5/7/2025, 11:03:16 PM
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res=[]
        for i in range(len(l)):
            n=sorted(nums[l[i]:r[i] + 1])
            j=2
            while j<len(n):
                if n[j]-n[j-1]!=n[1]-n[0]:
                    break
                j+=1
            res.append(j==len(n))

        return res
            