class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        print(tokens)
        for i in tokens:
            # print(s)
            if i == '+':
                r = s.pop(-1)
                l = s.pop(-1)
                s.append(l+r)
            elif i == '-':
                r = s.pop(-1)
                l = s.pop(-1)
                s.append(l-r)
            elif i == '*':
                r = s.pop(-1)
                l = s.pop(-1)
                s.append(l*r)
            elif i == '/':
                r = s.pop(-1)
                l = s.pop(-1)
                s.append(int(l/r))
            else:
                s.append(int(i))
        return s[0]
    