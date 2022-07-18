# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = self.dfs(root,[])
        return l[k-1]
    def dfs(self,root,l):
        # print(l)
        if not root:
            return l
        l = self.dfs(root.left,l)
        l.append(root.val)
        l = self.dfs(root.right,l)
        
        return l