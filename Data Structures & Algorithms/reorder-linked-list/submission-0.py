# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        ## slow is mid
        ## reversing it 
        prev = None
        curr = slow
        while curr.next:
            fut = curr.next
            curr.next = prev
            prev = curr
            curr = fut
        if curr.next==None:
            curr.next = prev

        dummy = head
        while curr.next and dummy.next:
            temp = dummy.next
            dummy.next = curr
            temp2 = curr.next
            curr.next = temp
            curr = temp2
            dummy = temp
        
        

        

        
        
        