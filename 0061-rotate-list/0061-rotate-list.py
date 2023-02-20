# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None or k==0:
            return head
        length=1
        curr=head
        while curr.next!=None:
            length+=1
            curr=curr.next
        
        curr.next=head
        rotations=int(k%length)
        rotations=length-rotations
        while rotations!=0:
            curr=curr.next
            rotations-=1
        head=curr.next
        curr.next=None
        return head
        