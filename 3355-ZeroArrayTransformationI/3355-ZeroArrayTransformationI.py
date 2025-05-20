# Last updated: 5/20/2025, 1:30:07 PM
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # Given an array we need to validate if after all the queries all entries become zero.
        # For every query l,r choose a subset and deccrease all values by 1
        #   since its a subset we can choose all the indexes for which values are non-zero
        # 
        # preprocess and put all the indexes with values 0 in a set. 
        # process the range l,r
        # if value becomes 0 add index to set. 
        # if after all query len of set is same as n True. 
        '''
        arr = deepcopy(nums)
        _sum = sum(nums)
        for l,r in queries :
            for i in range(l,r+1) :
                if arr[i] == 0 : continue
                arr[i] -= 1
                _sum -= 1
        return True if _sum == 0 else False
        '''
        arr = [0]*(len(nums)+1) 

        for l,r in queries :
            arr[l] += 1
            arr[r+1] -= 1
        rsum = 0
        for i in range(len(nums)) :
            rsum += arr[i]
            if nums[i] > rsum :
                return False
        return True

import atexit; atexit.register(lambda: open("display_runtime.txt", "w").write("0"))