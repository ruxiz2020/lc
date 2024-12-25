class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        O(N 2 ^ N)
        O(N 2 ^ N)
        """
        candidates.sort()
        print(candidates)
        res = []
        self.dfs(candidates, target, 0, res, [])
        return res

    def dfs(self, nums, target, index, res, path):

        print(target)
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):

            if i > index and nums[i] == nums[i-1]:
                print("continue")
                continue

            self.dfs(nums, target - nums[i], i + 1, res, path + [nums[i]])


candidates = [10,1,2,7,6,1,5]; target = 8
candidates = [1, 1, 6]; target = 8

ss = Solution()

res = ss.combinationSum2(candidates, target)

print(res) # [[1, 1, 6]]
