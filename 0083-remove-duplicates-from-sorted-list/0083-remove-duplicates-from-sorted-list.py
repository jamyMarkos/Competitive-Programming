# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashSet = set()
        prev, next_ = None, head
        while next_:
            if next_.val in hashSet:
                temp = next_.val
                while next_ and next_.val == temp:
                    next_ = next_.next
                prev.next = next_
            else:
                hashSet.add(next_.val)
                prev = next_
                next_ = next_.next
            
        return head
        