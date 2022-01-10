class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l + r) //2
            if t > nums[mid]:
                l = mid + 1
            elif t < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1
                