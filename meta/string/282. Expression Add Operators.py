class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        ans = []

        def dfs(start: int, prev: int, eval: int, path: list[str]) -> None:
            print(start, prev, eval, path)
            if start == len(num):
                if eval == target:
                    ans.append(''.join(path))
                return

            for i in range(start, len(num)):
                if i > start and num[start] == '0':

                    print(f"i {i}")
                    return
                s = num[start:i + 1]
                curr = int(s)
                if start == 0:
                    path.append(s)
                    dfs(i + 1, curr, curr, path)
                    path.pop()
                else:
                    for op in ['+', '-', '*']:
                        path.append(op + s)
                        if op == '+':
                            dfs(i + 1, curr, eval + curr, path)
                        elif op == '-':
                            dfs(i + 1, -curr, eval - curr, path)
                        else:
                            dfs(i + 1, prev * curr, eval - prev + prev * curr, path)
                        path.pop()

        dfs(0, 0, 0, [])
        return ans


num = "2032";
target = 8
res = Solution().addOperators(num, target)
print(res)  # ['2+0+3*2', '2-0+3*2']
