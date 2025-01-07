import collections
from typing import List


class Solution:
    """
    This code calculates the number of subarrays in an array nums that 
    sum to a given value 
    k by using a prefix sum and a hash map (counter) to track the 
    frequency of previously seen prefix sums.

    For each element in the array, it updates the running prefix sum, 
    checks if the difference between the current prefix and 
    k has been seen before (indicating a valid subarray), and increments 
    the result (ans) accordingly while updating the counter.
    O(N)
    O(N)
    """
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
