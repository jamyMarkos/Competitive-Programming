# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        H = []
        
        head = dummy = ListNode()

        for idx, node in enumerate(lists):
            if node:
                heappush(H, (node.val, idx))

        while H:
            val, idx = heappop(H)
            dummy.next = lists[idx]
            lists[idx] = lists[idx].next
            if lists[idx]:
                heappush(H, (lists[idx].val, idx))
            dummy = dummy.next

        return head.next