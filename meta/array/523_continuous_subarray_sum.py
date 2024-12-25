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

        # 'dp' is a list of sets, one set for each index in nums.
        # dp[i] will store all possible sums of subarrays that end at index i.
        dp = [set() for _ in range(len(nums))]

        # We iterate from i = 1 to the end of the nums list.
        # Why start at 1? Because we will look at dp[i-1] inside the loop.
        for i in range(1, len(nums)):

            # First, add the single element (nums[i-1]) as a possible sum ending at i-1.
            # This ensures dp[i-1] is not empty when we enter the inner loop.
            dp[i - 1].add(nums[i - 1])
            print(dp)  # Print the dp structure to observe how sums grow

            # For every sum we have stored in dp[i-1], we try to include nums[i]
            # to create new sums that end at index i.
            for num in dp[i - 1]:
                # curr_sum is the sum of the previous sums (num) plus the current element nums[i].
                curr_sum = nums[i] + num

                # Check if 'curr_sum' equals k or is a multiple of k (if k != 0).
                # If yes, we can return True immediately.
                if curr_sum == k or (k != 0 and curr_sum % k == 0):
                    print(curr_sum)  # Debug print if we found a valid subarray sum
                    return True

                # If it's not directly divisible, store it in dp[i] so that
                # future indices can build upon this sum.
                dp[i].add(curr_sum)
                print(dp)  # Debug print to see how dp[i] evolves

        # If we finish the loop without returning True, then no subarray sum
        # was a multiple of k.
        return False



ss = Solution()
nums = [23, 2, 6, 4, 7];
k = 6
res = ss.checkSubarraySum(nums, k)
print(res)  # True
