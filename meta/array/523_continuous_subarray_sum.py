


# naive dp, O(n^2), almost TLE
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dp = [set() for _ in range(len(nums))]
        for i in range(1, len(nums)):
            dp[i-1].add(nums[i-1])
            print(dp)
            for num in dp[i-1]:

                curr_sum = nums[i] + num
                if curr_sum == k or (k!= 0 and curr_sum % k == 0):
                    print(curr_sum)
                    return True
                dp[i].add(curr_sum)
                print(dp) # [{23}, {25, 2}, {8, 6, 31}, set(), set()]

        return False

ss = Solution()
nums = [23,2,6,4,7]; k = 6
res = ss.checkSubarraySum(nums, k)
print(res) # True
