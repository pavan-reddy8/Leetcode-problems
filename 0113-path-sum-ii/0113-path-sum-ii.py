# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
   
        def dfs(root,target,path):
            if not root:
                return
   
            path.append(root.val)
            if sum(path) == target and not root.left and not root.right:
                res.append(path.copy())
           
            dfs(root.left,target,path)
            dfs(root.right,target,path)
            path.pop()

    
        dfs(root,targetSum,[])
    
        return res
            