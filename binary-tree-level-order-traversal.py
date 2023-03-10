# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hash_table = defaultdict(list)
        if not root:
            return 
        
        def traverse(root, level):
            hash_table[level].append(root.val)

            if root.left:
                traverse(root.left, level + 1)
            if root.right:
                traverse(root.right, level + 1)

        traverse(root, 0)
        return hash_table.values()