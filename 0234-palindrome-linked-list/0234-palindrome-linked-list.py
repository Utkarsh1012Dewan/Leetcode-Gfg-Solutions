# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow,fast = head,head.next
        
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        nxt = slow.next
        
        prev = None
        
        while nxt:
            nxt_node = nxt.next
            nxt.next = prev
            prev = nxt
            nxt = nxt_node
        
        temp = head
        
        while prev:
            if temp.val != prev.val:
                return False
            temp = temp.next
            prev = prev.next
        
        return True