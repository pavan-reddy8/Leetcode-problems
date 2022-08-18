class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        visited = set()
        connected = 0
        for v1,v2 in edges:
            d[v1].append(v2)
            d[v2].append(v1)
        def dfs(v):
            visited.add(v)
            for vi in d[v]:
                if vi not in visited:
                    dfs(vi)
        for v in range(n):
            if v not in visited:
                connected += 1
                dfs(v)
        return connected
                