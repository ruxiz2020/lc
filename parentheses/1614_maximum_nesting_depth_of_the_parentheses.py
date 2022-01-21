class Solution:
    def maxDepth(self, s: str) -> int:

        stack = []

        max_depth = 0
        for c in s:
            if c == '(':
                stack.append(c)
                max_depth = max(max_depth, len(stack))
            elif c == ')':
                stack.pop()

        return max_depth
