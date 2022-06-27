class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre =[0] * len(nums)
        post =[0] * len(nums)
        answer = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                pre[0] = nums[0]
            else:
                pre[i] = pre[i-1] * nums[i]
        print(pre)
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1 :
                post[len(nums)-1] = nums[len(nums)-1]
            else:
                post[i] = post[i+1] * nums[i]
        print(post) 
        for i in range(len(nums)):
            if i == 0:
                answer[i] = post[i+1]
            elif i == (len(nums) - 1):
                answer[i] = pre[i-1]
            else:
                answer[i] = post[i+1] * pre[i-1]
        return answer
        
                
            