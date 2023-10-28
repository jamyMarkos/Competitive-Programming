# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum_left = 0

        def dfs(node, is_left):
            nonlocal sum_left

            if not node:
                return

            if not node.left and not node.right and is_left:
                sum_left += node.val

            dfs(node.left, True)
            dfs(node.right, False)

        dfs(root, False)

        return sum_left

            

            


            
        