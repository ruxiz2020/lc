class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, index, res, path):
        if path not in res:
            res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, res, path + [nums[i]])


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        O(N 2 ^N)
        """
        res = []
        nums.sort()

        subset = []
        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset[::])
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

            #decision not to include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, subset)

        dfs(0, [])
        return res

if __name__ == '__main__':

    nums = [1,2,2]

    ss = Solution()
    res = ss.subsetsWithDup(nums)

    print(res)
