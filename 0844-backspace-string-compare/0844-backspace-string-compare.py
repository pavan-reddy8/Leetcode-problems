class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        stack1 =[]
        for c in s:
            if c == "#" and stack:
                stack.pop()
            elif c != "#":
                stack.append(c)
        for c in t:
            if c == "#" and stack1:
                stack1.pop()
            elif c != "#":
                stack1.append(c)
        if stack == stack1:
            return True
        return False