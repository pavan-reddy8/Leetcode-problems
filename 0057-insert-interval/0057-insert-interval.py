class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = 0
        while l < len(intervals):
            if intervals[l][0] <= newInterval[0]:
                l+=1
            else:
                break
            
        intervals.insert(l,newInterval)
        print(intervals,l)
        l,r = 0,1
        res = [intervals[0]]
        while r < len(intervals):
            if res[l][1] >= intervals[r][0]:
                res[l][1] = max(intervals[r][1],res[l][1])
                r+=1
            else:
                res.append(intervals[r])
                l+=1
                r+=1
        return res