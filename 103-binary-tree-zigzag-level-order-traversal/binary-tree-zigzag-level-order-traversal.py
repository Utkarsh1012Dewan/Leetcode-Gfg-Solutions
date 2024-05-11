from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []

        ans = []
        leftToRight = True
        q = deque([root])

        while len(q) > 0:
            temp = deque()
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if leftToRight:
                    temp.append(node.val)
                else:
                    temp.appendleft(node.val)

                for child in [node.left,node.right]:
                    if child is not None:
                        q.append(child)
            
            ans.append(list(temp))
            leftToRight = not leftToRight
        
        return ans


        
        
        
        