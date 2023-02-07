# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and root2:
            return root2
        if root1 and not root2:
            return root1
        
        if not root1 and not root2:
            return None
        
        nnode = TreeNode(root1.val+root2.val)
        lnode = self.mergeTrees(root1.left,root2.left)
        rnode = self.mergeTrees(root1.right,root2.right)
        
        
        nnode.left = lnode
        nnode.right = rnode

        
        
        return nnode
        