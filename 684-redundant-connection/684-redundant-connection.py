class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = [0] * (len(edges)+1)
        rank = [1] * (len(edges))
        res = []
        for i in range(len(edges)+1):
            root[i] = i
        def rec(x):
            if root[x]==x:
                return x
            return rec(root[x])
        
        for [x,y] in edges:
            print(root)
            xr,yr = rec(x),rec(y)
            print(x,y,xr,yr)
            if xr==yr:
                return [x,y]
            elif x==xr:
                root[x]=yr
            elif y==yr:
                root[y]=xr
            else:
                root[xr] = yr
                