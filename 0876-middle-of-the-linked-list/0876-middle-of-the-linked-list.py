# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        len = 0
        
        while temp:
            len +=1
            temp = temp.next
            
        new = len//2
        
        temp1 = head
        
        while new:
            temp1 = temp1.next
            new-=1
        
        return temp1
        