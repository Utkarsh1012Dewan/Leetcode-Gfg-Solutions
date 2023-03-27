# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #optimised  
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
        
        return False
    
    
    
        #brute force
        
        track = {}
        
        while head:
            if head in track:
                return True
            track[head] = True
            head = head.next
        
        return False
        
        
        