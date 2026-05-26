# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast,slow=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        second=slow.next
        prev=None
        slow.next=None
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
            
        curr,second=head,prev
        while second:
            temp1,temp2=curr.next,second.next
            curr.next=second
            second.next=temp1
            second=temp2
            curr=temp1
        



        