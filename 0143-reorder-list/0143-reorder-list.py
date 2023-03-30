# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow,fast = head,head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        head2 = slow.next
        slow.next = None
        
        prev = None
        while head2:
            nxt = head2.next
            head2.next = prev
            prev = head2
            head2 = nxt
        
        
        first, second = head, prev
        while second:
            pnt1, pnt2 = first.next, second.next
            first.next = second
            second.next = pnt1
            first,second = pnt1, pnt2
            