class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            rem = target-nums[i]
            print(rem)
            if rem in seen:
                return [i,seen[rem]]
            else:
                seen[value]=i
                