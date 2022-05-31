class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        O(N ^M/T+1)
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


def combinationSum(self, candidates, target):
	def combination_sum(cur_ans, cur_sum, cand_idx):
        if cur_sum >= target:
            if cur_sum == target:
                ans.append(cur_ans)
            return
        for i in range(cand_idx, len(candidates)):
            combination_sum(cur_ans + [candidates[i]], cur_sum + candidates[i], i)
	ans = []
	combination_sum([], 0, 0)
	return ans


def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
	# BFS
	from collections import deque
	queue = deque() # [cur_target, cur_ans, cand_idx]
	queue.append((target, [], 0))
	ans = []
	while queue:
		cur_target, cur_ans, cand_idx = queue.popleft()
		for i in range(cand_idx, len(candidates)):
			new_target = cur_target - candidates[i]
			if new_target == 0:
				ans.append(cur_ans + [candidates[i]])
			elif new_target > 0:
				queue.append((cur_target - candidates[i], cur_ans + [candidates[i]], i))
	return ans
