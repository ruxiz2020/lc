import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix = 0
        count = collections.Counter({0: 1})

        for num in nums:
            prefix += num
            ans += count[prefix - k]
            count[prefix] += 1
            print(count)  # Counter({0: 1, 1: 1, 3: 1, 6: 1, 9: 1})

        return ans


nums = [1, 2, 3, 3];
k = 3
nums = [1, 2, 3];
k = 3
ss = Solution()
res = ss.subarraySum(nums, k)

print(res)  # 2
