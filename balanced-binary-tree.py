# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def heightBalanced(root):
            if not root:
                return [True, 0]
            left = heightBalanced(root.left)
            right = heightBalanced(root.right)

            if not left[0] or not right[0]:
                tmp = False
            else:
                tmp = abs(left[1] - right[1]) <= 1

            return [tmp, 1 + max(left[1], right[1])]

        res = heightBalanced(root)

        return res[0]