class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair=[]
        st=[]
        for i in range(len(position)):
            pair.append((position[i],speed[i]))
        pair.sort()

        for i in pair:
  
            
            if not st:
                st.append(i)
            else:
                if ((target-i[0])/i[1]) < ((target-st[-1][0])/st[-1][1]):
                    st.append(i)
                else:
                    while st and ((target-i[0])/i[1]) >= ((target-st[-1][0])/st[-1][1]):
                        del st[-1]
                    st.append(i)

        return len(st)
        