# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        start = head
        while start.next:
            count+=1
            start = start.next
        ## we got length in count
        prev = None
        start = head
        count = count - n
        if count==0:
            return head.next
        while count>0:
            count = count -1 
            prev = start
            start = start.next
        prev.next = start.next
        return head

        