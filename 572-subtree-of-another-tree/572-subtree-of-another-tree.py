# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        res =[False]
        def dfs(root,subroot):
            if root is None:
                return False
            if subroot is None:
                return True
            if  sametree(root,subroot):
                return True
            else:
                return dfs(root.left,subroot) or dfs(root.right,subroot)
            return False
        def sametree(root,subroot):
            if not root and not subroot:
                return True
            if root and subroot and root.val == subroot.val:
                l = sametree(root.left,subroot.left)
                r = sametree(root.right,subroot.right)
                return l and r
            return False
        
        return dfs(root,subroot)
        
        