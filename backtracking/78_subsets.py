class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        O(N 2 ^N)
        """
        res = []
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, index, res, path):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, res, path + [nums[i]])


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        O(N 2 ^N)
        """
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            #decision not to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

if __name__ == '__main__':

    nums = [1,2,3]

    ss = Solution()
    res = ss.subsets(nums)

    print(res)
