# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node =TreeNode()
        if root is None:
            return 
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        node.val = root.val
        node.left = left
        node.right = right
        return node
        
        
        