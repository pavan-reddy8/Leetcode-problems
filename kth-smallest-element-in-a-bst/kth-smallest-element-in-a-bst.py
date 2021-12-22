# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], l: int) -> int:
        self.k = l
        self.a = 0
        return self.ll(root)
    def ll(self,root):
        if root is not None and self.k >=0:
            self.ll(root.left)
            self.k -= 1
            print(self.a)
            if self.k == 0:
                self.a = root.val
                return self.a
            if self.k > 0:
                print("a")
                self.ll(root.right)
        return self.a