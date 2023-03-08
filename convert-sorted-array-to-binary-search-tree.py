# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]: 
        l, r = 0, len(nums) - 1
        def heightBalanced(l, r):
            mid = (l + r) // 2
            if l > r:
                return 
            root = TreeNode(nums[mid])
            root.left = heightBalanced(l, mid - 1)
            root.right = heightBalanced(mid + 1, r)
            return root


        return heightBalanced(l, r)