
class Solution(object):

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

    def rob(self, nums):
        if not nums:
            return 0

        return max(self.helper(nums[1:]), self.helper(nums[:-1])) if len(nums) > 2 else max(nums)


if __name__ == '__main__':

    nums = [2, 3, 2]

    ss = Solution()
    res = ss.rob(nums)
    print(res)
