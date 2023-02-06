# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(root):
            if not root:
                return [-1,0]
            [lheight,ldia] = dfs(root.left)
            [rheight,rdia] = dfs(root.right)
            
            return [1+max(lheight,rheight),max(lheight+rheight+2,ldia,rdia)]
        
        
        return dfs(root)[1]
        