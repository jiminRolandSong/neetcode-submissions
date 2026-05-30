class MinStack:

    def __init__(self):
        self.stack = []
        self.minnum = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minnum) > 0:
            current_min = self.minnum[-1]
            self.minnum.append(min(val, current_min))
        else:
            self.minnum.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minnum.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minnum[-1]
        
