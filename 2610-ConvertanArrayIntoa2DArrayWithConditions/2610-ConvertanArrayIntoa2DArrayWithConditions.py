# Last updated: 5/7/2025, 12:54:10 AM
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        has = {}
        for i in nums:
            if i in has:
                has[i]+=1
            else:
                has[i]=1
        max_freq = has[max(has,key=has.get)]
        ans = [[] for i in range(max_freq)]

        for i in nums:
            while has[i]>0:
                ans[has[i]-1].append(i)
                has[i]-=1
        return ans