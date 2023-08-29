# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #basically doing an inorder traversal but not storing the result in an array. Just keeping a number n and incrementing it until we reach k. As soon as we do we know cur is holding that kth element so we return that.
        n = 0
        stack = []
        
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur =  cur.left
            cur = stack.pop()
            n+=1
            if n == k:
                return cur.val
            cur = cur.right
        
        return res[k-1]        
        
        
        
        
        