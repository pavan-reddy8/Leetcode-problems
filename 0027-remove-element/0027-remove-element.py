class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        numscopy = copy.deepcopy(nums)
        for i in range(len(numscopy)):
            if numscopy[i] == val:
                nums.remove(val)
                
            else:
                k+=1

        return k
        