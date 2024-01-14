
class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for id in asteroids:
            if not stack or stack[-1] * id > 0 or stack[-1] < 0:
                stack.append(id)
            elif abs(id) >= abs(stack[-1]):
                while stack and stack[-1] > 0 and abs(id) > abs(stack[-1]):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(id)
                elif stack[-1] == -id:
                    stack.pop()
        return stack

class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)

        return stack
