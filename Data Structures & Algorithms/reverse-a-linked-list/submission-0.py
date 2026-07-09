# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head
        prev = None
        fut = None
        while curr.next !=None:
            fut = curr.next
            curr.next = prev
            prev = curr
            curr = fut
        if curr.next==None:
            head = curr
            curr.next = prev
        return head
        