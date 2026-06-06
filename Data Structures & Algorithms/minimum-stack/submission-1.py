class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minimum) < 1:
            self.minimum.append(val)
        else:
            minnum = min(self.minimum[-1], val)
            self.minimum.append(minnum)
        

    def pop(self) -> None:
        self.minimum.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        
