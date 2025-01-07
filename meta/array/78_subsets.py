class Solution(object):
    def subsets(self, nums):
        """
        This code generates all possible subsets of a list of integers by 
        recursively exploring each element's inclusion or exclusion.

        It maintains the current subset (path) in each recursion and 
        stores it in res before continuing to the next element.

        The time complexity is O(N 2 ^N) because there are 2 ^N
        subsets in total and constructing each subset can take up to O(N) time.

        O(N 2 ^N)
        O(N 2 ^N)
        """
        res = []
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, index, res, path):
        res.append(path)
        for i in  range(index, len(nums)):
            self.dfs(nums, i + 1, res, path + [nums[i]])


if __name__ == '__main__':

    nums = [1,2,3]

    ss = Solution()
    res = ss.subsets(nums)
    # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    print(res)
