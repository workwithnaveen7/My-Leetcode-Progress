# Last updated: 5/23/2025, 5:40:07 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val==t2.val and mirror(t1.left,t2.right) and mirror(t1.right,t2.left))
        if root:
            return mirror(root.left,root.right)
        else:
            return True