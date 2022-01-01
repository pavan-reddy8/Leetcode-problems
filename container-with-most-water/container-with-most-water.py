class Solution:
    def maxArea(self, h: List[int]) -> int:
        l = 0
        r = len(h)-1
        maxi = 0
        while l < r:
            if h[l] <= h [r]:
                maxi = max(maxi,h[l] *(r-l))
                l += 1
            else:
                maxi = max(maxi,h[r] *(r-l))
                r -= 1
        return maxi