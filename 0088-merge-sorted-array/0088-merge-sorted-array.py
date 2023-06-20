class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
    
        Do not return anything, modify nums1 in-place instead.
        """
        p1,p2 = 0,0
        p3 = 0
        num1copy = copy.deepcopy(nums1)
        
        while p1 < m and p2 < n:
            if num1copy[p1] < nums2[p2]:
                nums1[p3] = num1copy[p1]
                p1+=1
                p3+=1
            else:
                nums1[p3] = nums2[p2]
                p2+=1
                p3+=1
                
        while p1 < m:
            nums1[p3] = num1copy[p1]
            p1+=1
            p3+=1
        while p2 < n:
            nums1[p3] = nums2[p2]
            p2+=1
            p3+=1

                
            
        