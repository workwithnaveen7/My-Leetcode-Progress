# Last updated: 4/12/2025, 12:08:09 AM
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
    # def maxSum(self, A, B):
        i, j, n, m = 0, 0, len(nums1), len(nums2)
        a, b, mod = 0, 0, 10**9 + 7
        while i < n or j < m:
            if i < n and (j == m or nums1[i] < nums2[j]):
                a += nums1[i]
                i += 1
            elif j < m and (i == n or nums1[i] > nums2[j]):
                b += nums2[j]
                j += 1
            else:
                a = b = max(a, b) + nums1[i]
                i += 1
                j += 1
        return max(a, b) % mod