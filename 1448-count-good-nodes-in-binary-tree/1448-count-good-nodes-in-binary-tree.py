# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root,root.val)
    
    def dfs(self,root,m):
        if not root:
            return 0
        if root.val >= m: 
            l = self.dfs(root.left,root.val)
            print(root.val)
        else:
            l = self.dfs(root.left,m)
        if root.val >= m: 
            r = self.dfs(root.right,root.val)
            print(root.val)
            r+=1
        else:
            r = self.dfs(root.right,m)
            
        return l+r
            
        