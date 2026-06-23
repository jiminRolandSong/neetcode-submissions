from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.freqs = defaultdict(int)
        self.stack = []
        

    def push(self, val: int) -> None:
        self.freqs[val] += 1
        self.stack.append(val)
        

    def pop(self) -> int:
        mostfreq = max(self.freqs.values())

        savings = []

        while self.freqs[self.stack[-1]] != mostfreq:
            num = self.stack.pop()
            savings.append(num)
        
        result = self.stack.pop()
        self.freqs[result] -= 1

        for s in savings:
            self.stack.append(s)
        
        return result

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()