"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return None
        leftmost = root
         
        #this loop will update the levels
        while leftmost.left:
            head = leftmost

            #this loop will connect the pointers
            while head:
                head.left.next = head.right

                #checking whether there is another node on the same level(connecting right Node of first subtree to the left node of the second subtree on the same level)
                if head.next:
                    head.right.next = head.next.left
                #moving to the second node on the same level
                head = head.next
            #traversing to other nodes on left side
            leftmost = leftmost.left
        return root
