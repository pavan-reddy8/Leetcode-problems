# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avg = []
        q =deque()
        q.append(root)
        while(q):
            s = 0
            l = len(q)
            print(l)
            for i in range(0,l):
                s += q[0].val
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            avg.append(s/l)
        
        return avg