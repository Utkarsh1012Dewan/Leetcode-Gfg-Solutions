# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return None
        res = []
        queue = deque()
        if root:
            queue.append(root)
            
        
        while len(queue) > 0:
            temp = []
            
            for i in range(len(queue)):
                cur = queue.popleft()
                temp.append(cur.val)
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            res.append(temp[-1])
        
        return res
        
        
        
        
        
        
#         if not root:
#             return None
        
#         res = []
        
#         curr = root
        
#         while curr and curr.right:
#             res.append(curr.val)
#             curr = curr.right
        
#         return res
        