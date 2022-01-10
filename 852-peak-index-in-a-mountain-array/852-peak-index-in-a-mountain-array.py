class Solution:
    def peakIndexInMountainArray(self, a: List[int]) -> int:
        m = -1
        loc = -1
        for i in range(1 ,len(a)-1):
            if a[i-1]< a[i] > a[i+1]:
                m,loc = (a[i],i) if a[i] > m else (m,loc)
        return loc