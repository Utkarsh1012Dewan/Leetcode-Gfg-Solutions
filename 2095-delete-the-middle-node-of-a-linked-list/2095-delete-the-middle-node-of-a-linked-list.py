# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if the list is empty or has only one element, return the head
        if not head or not head.next:
            return None
        
        # Initialize two pointers: slow and fast
        slow, fast = head, head
        
        # Initialize a variable to keep track of the previous node
        prev = None
        
        # Traverse the list with the two pointers
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node by updating the next pointer of the previous node
        prev.next = slow.next
        
        # Return the head of the modified list
        return head
