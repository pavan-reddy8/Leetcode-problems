class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0, len(nums)-1
        while l <= r:
            while l<r and nums[l] == nums[l+1]:
                l+=1
            while l<r and nums[r-1] == nums[r]:
                r-=1
            mid = (l+r) // 2
            # print(l,r,mid)
            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid +1
                else:
                    r = mid -1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid +1
        return False
        