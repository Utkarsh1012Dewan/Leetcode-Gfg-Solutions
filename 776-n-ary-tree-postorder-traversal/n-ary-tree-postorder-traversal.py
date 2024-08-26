"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        def dfs(root,ans):
            for child in root.children:
                dfs(child,ans)
            ans.append(root.val)

        dfs(root,ans)
        return ans