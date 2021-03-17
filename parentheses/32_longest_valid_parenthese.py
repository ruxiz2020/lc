class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0

        stack = list()
        stack.append(-1)
        max_len = 0

        for idx, c in enumerate(s):
            if c == '(':
                stack.append(idx)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(idx)
                length = idx - stack[-1]
                if length > max_len:
                    max_len = length

        return max_len
