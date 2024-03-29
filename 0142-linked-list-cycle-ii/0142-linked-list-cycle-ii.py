# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return None
        
        
        slow = head
        fast = head
        entry = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                    
                if entry == slow:
                    return slow
        return None
        
        
        