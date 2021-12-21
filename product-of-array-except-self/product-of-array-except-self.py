class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = []
        p = 1
        for i in range(len(nums)):
            pro.append(p)
            p = p * nums[i]
        p=1
        for i in range(len(nums)-1,-1,-1):
            pro[i] = pro[i] * p
            p = p * nums[i]
        return pro
            
        