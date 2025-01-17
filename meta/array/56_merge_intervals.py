class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        O(nlogn)
        O(n)
        """
        if len(intervals) == 0:
            return []
        sorted_intervals = sorted(intervals, key=lambda x: x[0]) # O(nlogn)
        res = [sorted_intervals[0]]
        for interval in sorted_intervals[1:]:
            # the next node's smallest value is smaller than the prev node's largest value, then overlapping
            if interval[0] <= res[-1][1]:
                # left boundary is the largest value
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
res = Solution().merge(intervals)
print(res)  # [[1, 6], [8, 10], [15, 18]]
