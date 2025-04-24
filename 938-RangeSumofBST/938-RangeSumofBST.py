# Last updated: 4/25/2025, 1:14:31 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: # if root doesnt exist
            return 0 # return none
        if root.val > high: # if root.val is greater than high
            return self.rangeSumBST(root.left, low, high) # we call the function again with root.left
        elif root.val < low: # if root.val is less than low
            return self.rangeSumBST(root.right, low, high) # we call the function again with root.right
        else: # if the root.val lies between the range
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) # we call the function again with root.left and root.right