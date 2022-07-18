# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root,float(-inf),float(inf))
    def dfs(self,root,a,b):
        if not root:
            return True
        l = self.dfs(root.left,a,root.val)
        r = self.dfs(root.right,root.val,b)
        res = True
        if not (a < root.val < b):
            res = False
        return l and r and res
        