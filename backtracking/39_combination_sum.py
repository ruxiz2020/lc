class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        O(2 ** T)
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, res, [])
        return res


    def dfs(self, nums, target, index, res, path):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if nums[index] > target:
                return
            self.dfs(nums, target - nums[i], i, res, path + [nums[i]])



if __name__ == '__main__':

    candidates = [2,3,6,7]
    target = 7

    ss = Solution()
    res = ss.combinationSum(candidates, target)

    print(res)
