# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        cur =root
        res =[]
        q=Queue()
        if root is None:
            return res
        q.put(root)
        while not q.empty():
            n = q.qsize()
            for i in range(n):
                cur = q.get()
                if i is n-1:
                    res.append(cur.val)
                if cur.left is not None:
                    q.put(cur.left)
                if cur.right is not None:
                    q.put(cur.right)
        return res