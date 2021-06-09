class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(cur, k, n, tmp):
            if k == 0:
                if n == 0:
                    res.append(tmp[:])
                return
            for i in range(cur, 10):
                if i > n:
                    return
                tmp.append(i)
                dfs(i + 1, k - 1, n - i, tmp)
                tmp.pop()

        res = []
        dfs(1, k, n, [])
        return res
