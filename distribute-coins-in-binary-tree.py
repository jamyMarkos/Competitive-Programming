# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        num_moves = 0


        def dfs(cur_node):
            nonlocal num_moves

            if not cur_node:
                return 0

            left = dfs(cur_node.left)
            right = dfs(cur_node.right)

            num_moves += abs(left) + abs(right)

            return cur_node.val + left + right - 1

        dfs(root)


        return num_moves