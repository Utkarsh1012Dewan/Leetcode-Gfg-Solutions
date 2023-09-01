# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:


        def dfs(node,parent,depth,value):

            if node:
                if node.val == value:
                    return parent,depth
                return dfs(node.left,node,depth+1,value) or dfs(node.right,node,depth+1,value)
        
        parX,depX = dfs(root,None,0,x)
        parY,depY = dfs(root,None,0,y)

        return depX==depY and parX != parY










        