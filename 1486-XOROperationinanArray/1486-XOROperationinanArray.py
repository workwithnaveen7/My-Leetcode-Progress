# Last updated: 4/21/2025, 11:42:48 PM
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        first_value = start + 2 * 0 
        for i in range(1,n):
            first_value^= start + 2 * i  
        return first_value
        

        