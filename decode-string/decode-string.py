class Solution:
    def decodeString(self, s: str) -> str:
        temp = ""
        res = ""
        st =[]
        num = ""
        for c in s:
            print(c)
            print(st)
            if c.isdigit():
                num = num + c
            elif c is '[':
                st.append(int(num))
                num =''
                st.append(c)
                       
                
            elif c is ']':
                while st[-1] is not '[':
                    temp = st.pop() + temp
                    print(temp)
                st.pop()
                val = st.pop()
                print(val)
                print(temp)
                temp = temp * int(val)
                print(temp)
                st.append(temp)
                temp =''
            elif c:
                st.append(c)
        
        while(st):
            res = st.pop() + res
                
        return res