# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans, stack = [], []
        cur = head
        while cur:
            while stack and cur.val > stack[-1][1]:
                ans[stack.pop()[0]] = cur.val
            stack.append([len(ans), cur.val])
            ans.append(0)
            cur = cur.next
            
        return ans
                
        