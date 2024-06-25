# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #to keep a global sum of all the nodes
    val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
      if root:
        self.bstToGst(root.right)

        #1. we make the value of root = the sum of value of all the nodes
        #   that have a key valuie greater than itself

        #2.We also update the global sum with the new value of the root
        #   for other upcoming nodes
        root.val = self.val = self.val + root.val

        
        self.bstToGst(root.left)
        
        return root
        


        