class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negStone = [-stone for stone in stones]
        heapq.heapify(negStone)
        while len(negStone) > 1:
            stoney = negStone[0]
            heapq.heappop(negStone)
            stonex = negStone[0]
            heapq.heappop(negStone)
            if stonex != stoney:
                heapq.heappush(negStone,(stoney-stonex))
        if len(negStone):
            return -negStone[0]
        return 0