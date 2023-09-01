# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(root1,root2):

            if root1 == None and root2 == None:
                return True
            
            if (root1 and root2 == None) or (root1 == None and root2):
                return False
            
            if root1.val == root2.val:
                return dfs(root1.left,root2.right) and dfs(root1.right,root2.left)

        return dfs(root.left,root.right)



        # #My BFS approach
        # queue = deque()
        # if root:
        #     queue.append(root)
        
        # while queue:

        #     temp = []

        #     for i in range(len(queue)):
        #         cur = queue.popleft()
        #         if cur:
        #             temp.append(cur.val)
        #             queue.append(cur.left)
        #             queue.append(cur.right)
        #         else:
        #             temp.append(None)

        #     if len(temp)== 1:
        #         continue
        #     n = len(temp)
        #     for i in range(n//2):
        #         if temp[i] != temp[n-i-1]:
        #             return False
        # return True        