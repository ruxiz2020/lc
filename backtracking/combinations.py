class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        O(N!)
        """
        if len(nums) == 1:
            return [nums.copy()]
            
        res = []
        self.dfs(nums, res, [], 0)
        return res

    def dfs(self, nums, res, path, index):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], res, path + [nums[i]], index)


if __name__ == '__main__':

    nums = [1,2,3]

    ss = Solution()
    res = ss.permute(nums)

    print(res)
    print(len(res))
