class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        j = 0
        for i in range(len(intervals)):
            if i == 0:
                continue
            elif res[j][1] >= intervals[i][0]:
                res[j][1] = max(intervals[i][1],res[j][1])
            else:
                res.append(intervals[i])
                j+=1
        return res