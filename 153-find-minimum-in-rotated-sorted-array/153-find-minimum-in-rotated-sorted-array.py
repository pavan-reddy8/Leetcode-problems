class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mid = (l+r)//2
        res = nums[mid]
        while l <= r:
            mid = (l+r)//2
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            else:
                res = min(res,nums[mid])
                if nums[mid] >= nums[l]:
                    l = mid +1
                else:
                    r = mid -1
        return res
                    