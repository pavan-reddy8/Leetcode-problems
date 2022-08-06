"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        visited = set()
        h ={}
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            newNode = Node(node.val)
            h[node] = newNode
            
            for n in node.neighbors:
                dfs(n)
                newNode.neighbors.append(h[n])
        dfs(node)
        return h[node]
            
        # def dfs(node):
        #     visited.add(node)
        #     newNode = Node(node.val)
        #     for n in node.neighbors:
        #         if n not in visited:
        #             adjucent = dfs(n)
        #             newNode.neighbors.append(adjucent)
        #             adjucent.neighbors.append(newNode)
        #     return newNode
        # newstart = dfs(node)
        # cur = newstart
        # prev = newstart
        # visited = set()
        # while True:
        #     print(cur.val,prev.val)
        #     visited.add(cur)
        #     for n in cur.neighbors:
        #         if n not in visited:
        #             prev = cur
        #             cur = n
        #     if cur == prev :
        #         break
                    
                
        # return newstart
                
            
            
        