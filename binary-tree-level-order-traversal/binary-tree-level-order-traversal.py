# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = Queue()
        l = []
        q.put(root)
        ln =[]
        if root is None:
            return l
        ln.append(root.val)
        while not q.empty():
            l.append(ln)
            ln =[]
            n = q.qsize()
            for i in range(n):
                cur = q.get()
                if cur.left is not None or cur.right is not None:
                    if cur.left is not None:
                        q.put(cur.left)
                        ln.append(cur.left.val)
                    if cur.right is not None:
                        q.put(cur.right)
                        ln.append(cur.right.val)
        return l