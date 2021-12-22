class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        # i = 1
        # j = 0
        # k=0
        # ans = []
        # print(len(t))
        # while i < len(t):
        #     k+=1
        #     print(t[i-1],i-1,k)
        #     if t[i-1] < t[i]:
        #         i += 1
        #         ans.append(1)
        #         continue
        #     if (i+j) < len(t):
        #         if t[i-1] >= t[i+j]:
        #             j +=1
        #         else:
        #             ans.append(j+1) 
        #             j = 0
        #             i += 1
        #     else:
        #         ans.append(0)
        #         j = 0
        #         i += 1
        # ans.append(0)
        # return ans
        st = []
        ans = [0] * len(t)
        for i,v in enumerate(t):
            while st and  t[st[-1]] < v:
                ans[st[-1]] = i-st[-1]
                st.pop()
            st.append(i)
            
        return ans
                
                
                
            
            
            