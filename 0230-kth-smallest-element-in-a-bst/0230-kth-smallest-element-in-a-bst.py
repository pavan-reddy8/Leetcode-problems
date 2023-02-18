# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root,l):
            if not root :return l
            
            dfs(root.left,l)
            l.append(root.val)
            dfs(root.right,l)
            return l
        
        res = dfs(root,[])
        
        return res[k-1]