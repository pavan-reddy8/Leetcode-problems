class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal= nums[len(nums)-1]
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        if not goal:
            return True
        return False
        