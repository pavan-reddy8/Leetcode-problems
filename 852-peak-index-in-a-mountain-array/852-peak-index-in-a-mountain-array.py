class Solution:
    def peakIndexInMountainArray(self, a: List[int]) -> int:
        # m = -1
        # loc = -1
        # for i in range(1 ,len(a)-1):
        #     if a[i-1]< a[i] > a[i+1]:
        #         m,loc = (a[i],i) if a[i] > m else (m,loc)
        # return loc
        l,r =0,len(a)-1
        while l < r:
            mid = (l+r)//2
            if a[mid] < a[mid+1]:
                l = mid+1
            else:
                r=  mid
        return l