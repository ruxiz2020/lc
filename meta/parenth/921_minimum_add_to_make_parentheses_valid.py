class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        res = 0
        stack = []
        for c in S:
            if c == '(':
                stack.append('(')

            else:
                if stack:
                    stack.pop()
                else:
                    res += 1
        print(res, stack)
        return res + len(stack)


s = "())"
s = "((("

ss = Solution()
res = ss.minAddToMakeValid(s)
print(res)
