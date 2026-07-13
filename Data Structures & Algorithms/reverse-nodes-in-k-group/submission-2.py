# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:
            return head
        slow = head
        fast = head
        con = None
        L =0
        while True:
            n = k 
            while n>0 and fast:
                last = fast
                fast = fast.next
                n-=1
            if n>0:
                con.next=slow
                break
            prev = None
            if con==None:
                con=slow
            else:
                con.next = last
                con = slow
            while slow!=fast:
                temp = slow.next
                slow.next = prev
                prev = slow
                slow = temp
            if L==0:
                res = prev
            L+=1
        return res
            

