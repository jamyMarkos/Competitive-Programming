# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hash_table = defaultdict(int)
        def helper(root):
            hash_table[root.val] += 1

            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)
        
        helper(root)
        sorted_hash = sorted(hash_table.items(), key = lambda x: x[1], reverse=True)
        # answer = []
        # for val, key in sorted_hash:
        #     if key < sorted_hash[0][0]:
        #         break
        #     answer.append(val)
        # return answer
        # print(sorted_hash)
        print(sorted_hash)
        return [val for val, key in sorted_hash if key >= sorted_hash[0][1]]