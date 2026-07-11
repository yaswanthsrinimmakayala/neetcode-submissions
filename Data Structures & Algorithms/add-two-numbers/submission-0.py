# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2
        head =  ListNode(0)
        curr = head
        carry = 0
        while head1 and head2:
            num = head1.val+head2.val+carry
            carry = num//10
            num = num%10
            curr.next = ListNode(num)
            curr = curr.next
            head1 = head1.next
            head2 = head2.next
        if head1:
            while head1:
                num = head1.val+carry
                carry = num//10
                num = num%10
                curr.next = ListNode(num)
                curr = curr.next
                head1 = head1.next
        if head2:
            while head2:
                num = head2.val+carry
                carry = num//10
                num = num%10
                curr.next = ListNode(num)
                curr = curr.next
                head2 = head2.next
        if carry>0:
            curr.next = ListNode(carry)
        return head.next
        
        
