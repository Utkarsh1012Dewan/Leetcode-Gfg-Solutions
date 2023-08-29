# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        #slightly more efficient
        
        if not root:
            return None
        res = []
        
        queue = deque([root])
        
            
        while len(queue) > 0:
            rightNode = None
            
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    rightNode = cur
                    queue.append(cur.left)
                    queue.append(cur.right)
            if rightNode:
                res.append(rightNode.val)
        
        return res
          
        
        #My own approach
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
        

        