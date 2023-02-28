# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,bmin,bmax):
            if not root:
                return True
            if root.val <= bmin or root.val >= bmax:
                return False
            
            resleft = dfs(root.left,bmin,root.val)
            resright = dfs(root.right,root.val,bmax)
            
            return resleft and resright
        
        return dfs(root,float(-inf),float(inf))
            
            
        
        