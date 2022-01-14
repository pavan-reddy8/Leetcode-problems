# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return -1
            l = 1 + dfs(root.left)
            r = 1 + dfs(root.right)
            return max(l,r)
        return 1 + dfs(root)
    