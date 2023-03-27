# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Linear time + O(1) space comp. - N = 10^4
        
        # if len(LL) <= 2: We just have to return - no need to reorder!
        if not head or not head.next:
            return head
        
        half1 = even = head # half1 & half2 - will hold the start of both halfs of ordered list.
        half2 = odd = head.next 
        
        while even and even.next and even.next.next and odd:
            
            even.next = odd.next
            even = even.next
            odd.next = even.next
            odd = odd.next
            
        even.next = half2
        return half1
        
        
        
        
        
        
        