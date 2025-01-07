class Solution:
    """
    This code solves the "House Robber" problem by keeping track of two states, 
    where dp0 holds the best sum if the current house is not robbed, 
    and dp1 holds the best sum if the current house is robbed.

    At each house, it updates these two states, deciding whether to 
    include the current house’s amount (dp0 + nums[i]) or skip it (dp1).
    The algorithm runs in O(n) time and 
    O(1) space because it updates two variables in each step without storing additional structures.
    O(n)
    O(1)
    """
    def rob(self, nums):
        dp0 = dp1 = 0
        for i in range(len(nums)):
            dp0, dp1 = dp1, max(dp0 + nums[i], dp1)
        return dp1


if __name__ == '__main__':
    nums = [2,7,9,3,1]

    print("nums = [2,7,9,3,1]")

    ss = Solution()
    res = ss.rob(nums)

    print(res)
    # 12
