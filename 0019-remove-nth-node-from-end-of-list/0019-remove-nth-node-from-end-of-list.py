# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        nex = head
        
        while i < n:
            nex = nex.next
            i += 1
        
        prev = None
        cur = head
        while nex:
            prev, cur = cur, cur.next
            nex = nex.next
        if not prev:
            return head.next
        prev.next = cur.next
        
        return head
            
        