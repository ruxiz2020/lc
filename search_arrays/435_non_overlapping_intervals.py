class Solution:
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) == 0:
            return 0
        intervals.sort()
        now = intervals[0][1]
        res = 0
        for i in intervals[1:]:
            if i[0] < now:
                now = min(i[1], now)
                res += 1
            else:
                now = i[1]
        return res


if __name__ == '__main__':

    intervals = [[1,2],[2,3],[3,4],[1,3]]

    ss = Solution()
    res = ss.eraseOverlapIntervals(intervals)

    print(res)
