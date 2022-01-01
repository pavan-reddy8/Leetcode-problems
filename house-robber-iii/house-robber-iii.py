# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            li = [0]*2
            if root is None:
                return li
            l = dfs(root.left)
            r = dfs(root.right)   
            li[0] = root.val + l[1] + r[1]
            li[1] = max(l) + max(r)
            return li
        res = dfs(root)
        return max(res[0],res[1])