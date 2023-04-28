# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        ans = []
        ans.append(root.val / 1)
        
        while q:
            for i in range(len(q)):
                tt = q.popleft()
                if not tt:continue
                if tt.left:
                    q.append(tt.left)
                if tt.right:
                    q.append(tt.right)
                    
            if not len(q):
                break
            ans.append(sum([ptr.val for ptr in q if ptr]) / len(q))
            
        return ans
        