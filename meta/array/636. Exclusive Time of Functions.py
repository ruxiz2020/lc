from typing import List


class Solution:
    """
    This code calculates the exclusive execution time for each function in a system, 
    given a list of logs representing function calls and returns, 
    using a stack to track the currently active function and its start time.

    When a function starts, the time spent on the previously active function 
    (if any) is updated in the ans array, and the new function is added to the stack. 
    When a function ends, its total time is calculated (including the endpoint), 
    removed from the stack, and the current time is updated.
    O(m)
    O(n)
    """
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
                    ans[stk[-1]] += ts - curr  # task not finished, end excluded
                stk.append(fid)
                curr = ts
                print(stk) # [0] [0, 1]
            else:
                fid = stk.pop()
                ans[fid] += ts - curr + 1  # task finished, end included
                curr = ts + 1
        return ans


n = 2;
logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]

ss = Solution()

res = ss.exclusiveTime(n, logs)

print(res)  # [3, 4]
