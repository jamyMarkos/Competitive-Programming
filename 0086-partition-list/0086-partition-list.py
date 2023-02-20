# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr=head
        lst1=[]
        while(curr):
            lst1.append(curr.val)
            curr=curr.next
            
        dummyhead=ListNode()
        res=dummyhead
        
        for i in range(len(lst1)):
            if(lst1[i]<x):
                node=ListNode(lst1[i])
                res.next=node
                res=res.next
        for i in range(len(lst1)):
            if(lst1[i]>=x):
                node=ListNode(lst1[i])
                res.next=node
                res=res.next
                
        return dummyhead.next
        