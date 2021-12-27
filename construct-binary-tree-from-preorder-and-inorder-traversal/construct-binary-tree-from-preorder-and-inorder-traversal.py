# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, p: List[int], i: List[int]) -> Optional[TreeNode]:
        if not p and not i :
            return 
        root = TreeNode(p[0])
        r = i.index(p[0])
        root.left = self.buildTree(p[1:r+1],i[:r])
        root.right = self.buildTree(p[r+1:],i[r+1:])
        return root
