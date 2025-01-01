# naive dp, O(n^2), almost TLE
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool

        This function tries to determine if there exists a subarray (of length >= 2)
        in 'nums' such that the sum of its elements is a multiple of 'k'.

        Time Complexity (as written here): O(2^N) in the worst case
        Space Complexity: O(2^N) in the worst case
        """
        dp = [set() for _ in range(len(nums))]

        for i in range(1, len(nums)):

            dp[i - 1].add(nums[i - 1])
            print(dp)  # Print the dp structure to observe how sums grow

            for num in dp[i - 1]:
                # curr_sum is the sum of the previous sums (num) plus the current element nums[i].
                curr_sum = nums[i] + num

                if curr_sum == k or (k != 0 and curr_sum % k == 0):
                    print(curr_sum)  # Debug print if we found a valid subarray sum
                    return True

                dp[i].add(curr_sum)
                # [{23}, {25, 2}, {8, 6, 31}, set(), set()]
                print(dp)  # Debug print to see how dp[i] evolves

        return False



ss = Solution()
nums = [23, 2, 6, 4, 7]
k = 6
res = ss.checkSubarraySum(nums, k)
print(res)  # True
