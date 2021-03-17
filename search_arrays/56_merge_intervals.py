class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        O(nlogn)
        """
        if not intervals: return []
        # First sort the array lexicographically
        intervals = sorted(intervals)

        # Pairwise comparison
        start, end = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            curStart, curEnd = intervals[i]
            if curStart <= end:
                end = max(end, curEnd)
            else:
                res.append([start, end])
                start = curStart
                end = curEnd

        res.append([start, end])

        return res
