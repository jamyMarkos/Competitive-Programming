# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkSymmetry(l, r):
            if not l and not r:
                return True
            if not l or not r or l.val != r.val: 
                return False

            return checkSymmetry(l.left, r.right) and checkSymmetry(l.right, r.left)

        return checkSymmetry(root.left, root.right)