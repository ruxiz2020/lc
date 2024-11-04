from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stk = []
        curr = -1
        for log in logs:
            t = log.split(':')
            fid = int(t[0])
            ts = int(t[2])
            if t[1] == 'start':
                if stk:
                    ans[stk[-1]] += ts - curr
                stk.append(fid)
                curr = ts
                print(stk)
            else:
                fid = stk.pop()
                ans[fid] += ts - curr + 1
                curr = ts + 1
        return ans


n = 2; logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

ss = Solution()

res = ss.exclusiveTime(n, logs)

print(res)
