# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #basically the idea is agar tree ko niche se dekhoge, to jo ancestor sabse upar milega vo lowest common hoga because hum tree ko upar se hi dekhte hain.
        # agar dono p or q root se bade hain to rifht varna left
        # agar kisi bhi point pe dono sathme bade ya chote nahi hue to matlab vaha split hoga. That is the 
        #Lowest common ancestor node
        
        curr = root
        
        while curr:
            
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:    
                return curr
        
                
        
        
        
        