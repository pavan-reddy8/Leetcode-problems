# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        l = self.depth(root)
        if l[1] <= 1:
            return True
        return False
        
    def depth(self,root):
        if not root:
            return [0,0]
        l = self.depth(root.left)
        r = self.depth(root.right)
        return [1 + max(l[0],r[0]) , max(l[1],r[1],abs(l[0]-r[0]))]
        
        