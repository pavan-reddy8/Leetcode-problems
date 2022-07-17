# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        l =[]
        l.append(None)
        l.append(root)
        res = []
        n =[]
        debug = [None,root.val]
        while l:
            # print(debug)
            cur = l.pop(0)
            if cur:
                if cur.left:
                    l.append(cur.left)
                    debug.append(cur.left.val)
                if cur.right:
                    l.append(cur.right)
                    debug.append(cur.right.val)
            else:
                if l:
                    l.append(None)
                    debug.append(None)
        for i in debug:
            if i is None:
                if n:
                    res.append(n)
                n = []
            else:
                n.append(i)
        return res
                    

            
        