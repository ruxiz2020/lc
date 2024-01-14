class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            else:  # stack[-1][0] == c
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()

        print(stack)
        return ''.join(c * count for c, count in stack)


if __name__ == '__main__':
    s = "deeedbbcccbdaa"; k = 3

    ss = Solution()
    res = ss.removeDuplicates(s, k)

    print(res)
