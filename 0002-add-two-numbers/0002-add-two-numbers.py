# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = cur =ListNode(0)
        carry = 0

        while l1 or l2:
            
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            total = x + y + carry
            cur.next = ListNode(total % 10)

            carry = total // 10
          
            if l1: l1 = l1.next
            if l2: l2 = l2.next
           
            cur = cur.next
            
        
        if carry: cur.next = ListNode(carry)
        
        return dummyNode.next