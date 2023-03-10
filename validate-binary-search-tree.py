# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_validate(root, lower, upper):
            if not root:
                return True
            if lower >= root.val or upper <= root.val:
                return False
            else:
                return check_validate(root.left, lower, root.val) and check_validate(
                    root.right, root.val, upper
                )

        return check_validate(root, -math.inf, math.inf)