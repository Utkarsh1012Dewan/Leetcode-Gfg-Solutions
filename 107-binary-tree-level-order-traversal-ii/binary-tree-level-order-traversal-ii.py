# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        queue = deque()

        if root:
            queue.append(root)

        
        while queue:
            temp = []

            for i in range(len(queue)):
                cur = queue.popleft()
                temp.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            res.append(temp)
        
        return res[::-1]