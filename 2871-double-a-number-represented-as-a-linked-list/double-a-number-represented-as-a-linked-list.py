class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        stack = [dummy]

        while head:
            stack[-1].next = head
            stack.append(head)
            head = head.next

        carry = 0

        while stack:
            curr = stack.pop()
            newVal = (curr.val * 2) + carry 

            if newVal >= 10:
                carry = newVal // 10
            else:
                carry = 0
            curr.val = newVal % 10

        # Add a new node at the beginning if there's a carry left
        if carry > 0:
            newNode  = ListNode(carry)
            newNode.next = dummy.next
            dummy.next = newNode

        return dummy.next if dummy.val == 0 else dummy
