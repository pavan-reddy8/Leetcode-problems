class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        d={}
        for i in range(len(nums)):
            d[nums[i]]=i
        for i in range(len(nums)):
            if(d.get(target-nums[i])):
                if i != d[target-nums[i]]:
                    res += [i,d[target-nums[i]]]
                    break
        return res
            
        