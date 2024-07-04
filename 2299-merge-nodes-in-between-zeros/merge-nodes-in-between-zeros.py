# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        tail = dummy
        
        track = head.next
        total = 0

        while track:
            if track.val == 0:
                head.next.val = total
                total = 0
                head = head.next
            else:
                total += track.val
            track = track.next

        head.next = None
        return dummy.next.next
        