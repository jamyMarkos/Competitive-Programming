# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        hash_map = defaultdict(int)
        if not root:
            return []
        def helper(root, level):
            hash_map[level] = root.val

            if root.left:
                helper(root.left, level + 1)
            if root.right:
                helper(root.right, level + 1)
        
        helper(root, 0)
        print(hash_map)
        return list(hash_map.values())