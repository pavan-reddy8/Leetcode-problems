class Solution:
    def intervalIntersection(self, list1: List[List[int]], list2: List[List[int]]) -> List[List[int]]:
        
        res = []
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            
            if list1[i][1] >= list2[j][0] and list2[j][1] >= list1[i][0]:
                res.append([max(list1[i][0],list2[j][0]),min(list1[i][1],list2[j][1])])
                
            
            if list1[i][1] > list2[j][1]:
                j+=1
            elif list1[i][1] < list2[j][1]:
                i+=1
            else:
                j+=1
                i+=1
        return res
                