# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        # Find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
         
        # Invert right-hand half   
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        left, right = head, prev
        
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True
            
        