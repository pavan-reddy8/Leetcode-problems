# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (not q and p):
            return False
        if not p and not q:
            return True
        l = self.isSameTree(p.left,q.left)
        r = self.isSameTree(p.right,q.right)
        
        if p.val == q.val:
            return l and r
        return False
        
        