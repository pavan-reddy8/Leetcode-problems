# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dia = 0 
    def dfs(self,root):
        if root is None:
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.dia = max(self.dia,l+r)
        return 1+max(l,r)
        
            
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.dfs(root)
        return self.dia
        