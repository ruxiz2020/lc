class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O(n ** 2)
        """
        if not nums: return 0
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):

            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == '__main__':

    nums = [10,9,2,5,3,7,101,18]

    ss = Solution()
    res = ss.lengthOfLIS(nums)

    print(res)
