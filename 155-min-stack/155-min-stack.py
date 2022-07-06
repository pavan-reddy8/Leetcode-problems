class MinStack:
    def __init__(self):
        self.stack =[]
        self.minst = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minst:
            mini = min(val,self.minst[-1])
            if mini == val:
                self.minst.append(mini)
        else:
            self.minst.append(val)

    def pop(self) -> None:
        if self.minst[-1] == self.stack[-1]:
            del self.minst[-1]
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return(self.minst[-1])


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()