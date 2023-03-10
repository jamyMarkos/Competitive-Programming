# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def helper(root, local_path):
            if not root:
                return
            if not root.left and not root.right:
                paths.append(local_path + [root.val])
                return 
            helper(root.left, local_path + [root.val])
            helper(root.right, local_path + [root.val])

        helper(root, [])
        return ['->'.join(map(str, path)) for path in paths]