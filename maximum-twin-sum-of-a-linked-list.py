# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        cur, count = head, 0
        while cur:
            stack.append(cur.val)
            cur = cur.next
            count += 1

        max_twin = 0
        for i in range(count // 2):
            max_twin = max((stack.pop()+stack[i]), max_twin)
        return max_twin