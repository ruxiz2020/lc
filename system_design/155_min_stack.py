class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-5);
minStack.push(-4);

print(minStack.stack)
print(minStack.minStack)

p0 = minStack.getMin(); # return -3
print(p0)

minStack.pop();
print(minStack.stack)
print(minStack.minStack)

p2 = minStack.top();    # return 0
print(p2)
p3 = minStack.getMin(); # return -2
print(p3)
