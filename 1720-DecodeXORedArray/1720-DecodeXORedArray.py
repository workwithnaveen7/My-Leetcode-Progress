# Last updated: 6/9/2025, 10:10:08 PM
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr=[first]
        for i in range(len(encoded)):
            arr.append(arr[i] ^ encoded[i])
        return arr