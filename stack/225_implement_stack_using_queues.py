from collections import deque


class Stack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        # Add the element to queue1
        self.queue1.append(x)

    def pop(self):
        # Move all elements except the last one from queue1 to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        # Pop and return the last element from queue1
        popped_element = self.queue1.popleft()

        # Swap queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

        return popped_element

    def top(self):
        # Move all elements except the last one from queue1 to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        # Get and save the last element from queue1
        top_element = self.queue1.popleft()

        # Move the saved element to queue2
        self.queue2.append(top_element)

        # Swap queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

    def empty(self):
        return not self.queue1

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Top element:", stack.top())  # Output: 3
print("Pop:", stack.pop())          # Output: 3
print("Is the stack empty?", stack.empty())  # Output: False
