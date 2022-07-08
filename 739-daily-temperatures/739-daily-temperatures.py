class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        st =[]
        res =[0]*len(temps)
        for i,temp in enumerate(temps):

            while st and temps[st[-1]] <  temp :
                pos = st.pop(-1)
                res[pos] = i - pos
            st.append(i)
        return res