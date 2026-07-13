# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def mergeList(self,head1,head2):
        if head1==None and head2==None:
            return None
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        dummy = ListNode()
        head = dummy
        while head1 and head2:
            if head1.val<=head2.val:
                dummy.next = head1
                dummy = head1
                head1 = head1.next
            else:
                dummy.next = head2
                dummy = head2
                head2 = head2.next
        if head1:
            dummy.next = head1
        if head2:
            dummy.next = head2
        return head.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        for i in range(1,len(lists)):
            head1 = lists[i-1]
            head2 = lists[i]
            lists[i] = self.mergeList(head1,head2)
        return lists[-1]
