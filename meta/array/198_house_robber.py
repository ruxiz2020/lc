class Solution:
    """
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
