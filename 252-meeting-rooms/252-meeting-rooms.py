class Solution:
    def canAttendMeetings(self, l: List[List[int]]) -> bool:
        l.sort()
        for i in range(1,len(l)):
            if l[i-1][1] > l[i][0]:
                return False
        return True
        