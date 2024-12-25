from typing import List


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        Catalan(n) = (2n)!/((n+1)!*n!)
        O(n)
        """
        res = []
        self.dfs(res, n, n, '')
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + '(')
        if left < right:
            self.dfs(res, left, right - 1, path + ')')

class Solution01:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)

                stack.pop()
                print(stack)
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)

                stack.pop()
                print(stack)

        backtrack(0, 0)
        return res


class Solution02:
    def generateParenthesis(self, n: int) -> List[str]:

        self.res = []
        def helper(o, c, s=''):
            if o > c:
                return
            if o == 0 and c == 0:
                self.res.append(s)
                return
            if o == 0:
                helper(o, c - 1, s + ")")
            else:
                helper(o - 1, c, s + "(")
                helper(o, c - 1, s + ")")


        helper(n, n, '')
        return list(set(self.res))


if __name__ == '__main__':

    n = 3

    ss = Solution01()
    res = ss.generateParenthesis(n)

    print(res)# ['((()))', '(()())', '(())()', '()(())', '()()()']

    # n = 2
    # ss = Solution02()
    # res = ss.generateParenthesis(n)
    #
    # print(res)
    #
    # n = 4
    # ss = Solution02()
    # res = ss.generateParenthesis(n)
    #
    # print(res)
