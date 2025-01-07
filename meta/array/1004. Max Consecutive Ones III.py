class Solution:
    """
    This code finds the longest subarray containing at most 
    k zeros in a binary array nums using the sliding window technique,
    where two pointers (l and r) define the window and dynamically 
    adjust as the count of zeros exceeds 

    When a zero is encountered, 
    k is decremented, and if 
    k becomes negative, the left pointer (l) is advanced to shrink 
    the window until the number of zeros within the window is 
    ≤k, ensuring the constraint is maintained.
    O(N)
    O(1)
    """
    def longestOnes(self, nums: list[int], k: int) -> int:
        ans = 0

        l = 0
        for r, num in enumerate(nums):
            if num == 0:
                k -= 1
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans


nums = [1,1,1,0,0,0,1,1,1,1,0]; k = 2

res = Solution().longestOnes(nums, k)
print(res)# 6
