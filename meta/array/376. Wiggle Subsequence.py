import itertools


class Solution:
    """
    This code computes the length of the longest wiggle subsequence in an array nums,
      where a wiggle sequence alternates between increasing and decreasing values,
        by maintaining two counters: increasing and decreasing.

    For each adjacent pair of elements, it updates the counters based on 
    whether the current pair represents an increase or a decrease, 
    incrementing the opposite counter to reflect a valid wiggle transition.
    O(N)
    O(1)
    """
    def wiggleMaxLength(self, nums: list[int]) -> int:
        increasing = 1
        decreasing = 1

        pairs = list(zip(nums[:-1], nums[1:]))
        for a, b in pairs:
            if b > a:
                increasing = decreasing + 1
            elif b < a:
                decreasing = increasing + 1

        return max(increasing, decreasing)


nums = [1, 7, 4, 9, 2, 5, 6, 5]
res = Solution().wiggleMaxLength(nums)
print(res) # 7
