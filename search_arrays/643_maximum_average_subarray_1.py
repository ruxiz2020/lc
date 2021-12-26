class Solution:
    def findMaxAverage(self, nums, k):
        if not nums:
            return 0
        cur = res = sum(nums[:k])
        start = 0
        for end in range(k, len(nums)):
            cur += -nums[start] + nums[end]
            start += 1
            res = max(cur, res)
        return res / k


if __name__ == '__main__':

    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    ss = Solution()
    res = ss.findMaxAverage(nums, k)

    print(res)
