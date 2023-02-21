# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = dummyNode = ListNode()
        
        while list1 and list2:
            l1, l2 = list1.val, list2.val
            
            if l1 < l2:
                dummyNode.next = list1
                list1 = list1.next
            else:
                dummyNode.next = list2
                list2 = list2.next
            dummyNode = dummyNode.next
        if list1:
            dummyNode.next = list1
        if list2:
            dummyNode.next = list2
            
        return newHead.next
        