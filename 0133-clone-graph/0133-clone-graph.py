"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        s = {}
        def dfs(node):
            if not node:
                return None
            
            newNode = Node(node.val)
            s[node] = newNode
            for n in node.neighbors:
                if n not in s:
                    neigh = dfs(n)
                newNode.neighbors.append(s[n])
            return newNode
        
        return dfs(node)
                
                
            
   
                
            
            
        