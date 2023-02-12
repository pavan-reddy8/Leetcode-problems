class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redAdjList, blueAdjList = defaultdict(list), defaultdict(list)
        for u,v in redEdges:
            redAdjList[u].append(v)
        for u,v in blueEdges:
            blueAdjList[u].append(v)

        visitedBlue, visitedRed = set(), set()
        dist = [-1] * n
        dist[0] = 0
        queue = deque([[0, 0, None]])
        visitedBlue.add(0)
        visitedRed.add(0)
        while queue:
            u, d, c = queue.popleft()
            if not c or c == 'B':
                for v in redAdjList[u]:
                    if v in visitedRed:
                        continue
                    dist[v] = d+1 if dist[v] == -1 else min(dist[v], d+1)
                    queue.append([v, d+1,'R'])
                    visitedRed.add(v)
            if not c or c == 'R':
                for v in blueAdjList[u]:
                    if v in visitedBlue:
                        continue
                    dist[v] = d+1 if dist[v] == -1 else min(dist[v], d+1)
                    queue.append([v, d+1,'B'])
                    visitedBlue.add(v)
        return dist
        