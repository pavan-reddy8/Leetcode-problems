# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = [False]
        s =[0]
        def dfs(root):
            if root is None:
                return
            s[0] += root.val
            left = dfs(root.left)
            right = dfs(root.right)
            if not left and not right:
                if targetSum == s[0] :
                    res[0] = True
            s[0] -= root.val
            return root.val
        dfs(root)
        return res[0]