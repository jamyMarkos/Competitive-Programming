# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append([0, root])
        max_wid = 1
        
        while q:
            for i in range(len(q)):
                col, cur = q.popleft()
                if cur.left:
                    q.append([2 * col - 1, cur.left])
                if cur.right:
                    q.append([2 * col + 1, cur.right])
            if q:     
                max_wid = max(max_wid, (q[-1][0] - q[0][0]) // 2 + 1)
            
        return max_wid
        
        