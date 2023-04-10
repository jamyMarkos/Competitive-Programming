# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge-case and sanity test:
        if not head or not head.next:
            return head
        
        newHead = ll = ListNode()
        rr = head
        
        while rr and rr.next:
            
            if rr.val != rr.next.val:
                ll.next = rr
                ll = ll.next
                rr = rr.next
                
            else:
                while rr and rr.next and rr.val == rr.next.val:
                    rr = rr.next
                rr = rr.next
                ll.next = rr
        
        return newHead.next
        