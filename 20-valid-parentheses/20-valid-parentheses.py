class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            
            if c in ['(','{','[']:
                stack.append(c)
            elif len(stack) != 0:
                if c == ')' and stack[-1] == '(':
                    del stack[-1]
                elif c == '}' and stack[-1] == '{':
                    del stack[-1]
                elif c == ']' and stack[-1] == '[':
                    del stack[-1]
                else:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        return False