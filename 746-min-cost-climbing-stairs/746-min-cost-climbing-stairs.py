class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = 0
        i = len(cost) - 1
        while i >= 0:
            if i+1 > len(cost) -1:
                i-=1
                continue
            else:
                if i+2 <= len(cost) -1:
                    cost[i] = min(cost[i]+cost[i+1],cost[i]+cost[i+2])
                else:
                    cost[i] = min(cost[i],cost[i]+cost[i+1])
            i-=1
    
        return min(cost[0],cost[1])
        
        