class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
Let NN be the size of the input array.

Time Complexity: O(2^N)

In the worst case, our algorithm will exhaust all possible combinations from the input array, which in total amounts to 2^N2
Nas we discussed before.

The sorting will take \mathcal{O}(N \log N)O(NlogN).

To sum up, the overall time complexity of the algorithm is dominated by the backtracking process, which is \mathcal{O}(2^N)O(2
N
 ).

Space Complexity: \mathcal{O}(N)O(N)

We use the variable comb to keep track of the current combination we build, which requires \mathcal{O}(N)O(N) space.

In addition, we apply recursion in the algorithm, which will incur additional memory consumption in the function call stack. In the worst case, the stack will pile up to \mathcal{O}(N)O(N) space.

To sum up, the overall space complexity of the algorithm is \mathcal{O}(N) + \mathcal{O}(N) = \mathcal{O}(N)O(N)+O(N)=O(N).

Note: we did not take into account the space needed to hold the final results of combination in the above analysis.
        """
        candidates.sort()
        print(candidates)
        res = []
        self.dfs(candidates, target, 0, res, [])
        return res

    def dfs(self, nums, target, index, res, path):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        for i in xrange(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target - nums[i], i + 1, res, path + [nums[i]])
