class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        index_remove=set()
        res=""
        for i, v in enumerate(s):
            if v == "(":
                stack.append(i)
            else:
                left_index = stack.pop()
                if not stack:
                    index_remove.add(left_index)
                    index_remove.add(i)
        for i, v in enumerate(s):
            if i not in index_remove:
                res+=v
        return res

if __name__ == '__main__':

    s = "(()())(())"

    ss = Solution()
    res = ss.removeOuterParentheses(s)

    print(res)
