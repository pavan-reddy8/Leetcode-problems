# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        l =[]
        def pre(root):
            if root is None:
                return
            l.append(root)
            pre(root.left)
            pre(root.right)
            
        pre(root)
        for i in range(len(l)) :
            l[i].left = None
            if i+1 < len(l):
                l[i].right = l[i+1]
            else:
                l[i].right = None
            