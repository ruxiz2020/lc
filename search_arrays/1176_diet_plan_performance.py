from itertools import accumulate
from typing import List


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        s = list(accumulate(calories, initial=0))
        print(s)
        ans, n = 0, len(calories)
        for i in range(n - k + 1):
            print(i)
            t = s[i + k] - s[i]
            if t < lower:
                ans -= 1
            elif t > upper:
                ans += 1
        return ans

if __name__ == '__main__':

    calories = [1,2,3,4,5]; k = 1; lower = 3; upper = 3
    #calories = [6,5,0,0]; k = 2; lower = 1; upper = 5
    ss = Solution()
    res = ss.dietPlanPerformance(calories, k, lower, upper)
    print(res)
