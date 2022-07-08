class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums, target):
            l,r = 0,len(nums)-1
            while l<=r:
                p = (l+r)//2
                if nums[p] == target:
                    return p
                elif nums[p] < target:
                    l = (p)+1
                else:
                    r = (p)-1
            return -1
        for i in matrix:
            val = search(i,target)
            if  val != -1:
                return True
        return False