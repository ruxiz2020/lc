class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 放在这里
        visited = [False] * len(nums)
        ans = 0
        for i in xrange(len(nums)):
            road = 0
            while not visited[i]:
                road += 1
                # 下面两行的顺序不能变
                visited[i] = True
                i = nums[i]
            ans = max(ans, road)
        return ans
