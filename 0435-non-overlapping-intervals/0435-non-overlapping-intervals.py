class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        for i in range(len(intervals)):
            if i == 0:
                continue
            else:
                if intervals[i-1][1] > intervals[i][0]  :
                    res+=1
                    if intervals[i-1][1] < intervals[i][1]:
                        intervals[i] = intervals[i-1]
        return res