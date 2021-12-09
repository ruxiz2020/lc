class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) % 2 == 0 or len(nums) == 1:
            return True

        dp = [0] * len(nums)
        for i in reversed(range(len(nums))):
            print(i)
            dp[i] = nums[i]
            for j in range(i+1, len(nums)):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[-1] >= 0


if __name__ == '__main__':

    nums = [1,5,233,7]

    ss = Solution()
    res = ss.PredictTheWinner(nums)

    print(res)
