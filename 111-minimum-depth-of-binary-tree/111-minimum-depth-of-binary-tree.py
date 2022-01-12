# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            if l == 0 and r == 0:
                return 1
            if l == 0:
                return 1+r
            if r == 0:
                return 1+l
            print(l,r)
            return 1 +min(l,r)
                
        return dfs(root)
        