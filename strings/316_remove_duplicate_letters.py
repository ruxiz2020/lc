class Solution:
    def removeDuplicateLetters(self, s):
        stack = []
        seen = set()
        last = {c: i for i, c in enumerate(s)}
        print(last)
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last[stack[-1]]:
                    seen.remove(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)


if __name__ == '__main__':

    s = "cbacdcbc"

    ss = Solution()
    res = ss.removeDuplicateLetters(s)
    print(res)
