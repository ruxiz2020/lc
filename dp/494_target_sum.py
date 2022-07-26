class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        too slow
        """
        def helper(index, acc):
            if index == len(nums):
                if acc == S:
                    return 1
                else:
                    return 0
            return helper(index + 1, acc + nums[index]) + helper(index + 1, acc - nums[index])
        return helper(0, 0)


import collections
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        _len = len(nums)
        dp = [collections.defaultdict(int) for _ in range(_len + 1)]
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for sum, cnt in dp[i].items():
                dp[i + 1][sum + num] += cnt
                dp[i + 1][sum - num] += cnt
        print(dp)
        return dp[_len][S]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                              backtrack(i + 1, total - nums[i]))
            return dp[(i, total)]
        return backtrack(0, 0)


if __name__ == '__main__':

    nums = [1,1,1,1,1]; target = 3

    ss = Solution()
    res = ss.findTargetSumWays(nums, target)

    print(res)
