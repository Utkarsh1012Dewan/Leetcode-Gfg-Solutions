# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.next == None:
            return head

        fast = head.next
        slow = head

        while fast:
            val1 = fast.val
            val2 = slow.val

            gcd = math.gcd(val1,val2)
            node = ListNode(gcd,fast)
            slow.next = node

            fast = fast.next
            slow = slow.next.next
        
        return head
        