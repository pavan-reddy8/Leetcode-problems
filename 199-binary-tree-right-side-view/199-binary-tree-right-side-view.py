# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        l = [root]
        res = []
        while l:
            qlen = len(l)
            while qlen:

                cur = l.pop(0)

                if cur.left:
                    l.append(cur.left)
                if cur.right:
                    l.append(cur.right)
                if qlen ==1:
                    res.append(cur.val)
                qlen -=1
        return res
                
        