from typing import List


class Solution:
    """
    O(n)
    O(1)
    """
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums) # O(n)
        return expected_sum - actual_sum


nums = [3,0,1]
ss = Solution()
res = ss.missingNumber(nums)
print(res) # 2
