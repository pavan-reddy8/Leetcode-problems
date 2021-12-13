class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        bol = [False] * (len(nums))
        for num in nums:
            bol[num-1] = True

        for i,j in enumerate(bol):
            if not j:
                res.append(i+1)
        # print(bol)
        return res
                
        