import bisect

class Solution:
    def findRightInterval(self, intervals):
        intervals = sorted((e[0], i, e[1]) for i, e in enumerate(intervals))
        print(intervals)
        l = len(intervals)
        res = [0] * l
        for e in intervals:
            r = bisect.bisect_left(intervals, (e[2], ))
            res[e[1]] = intervals[r][1] if r < l else -1
        return res


if __name__ == '__main__':

    intervals = [[1,4],[2,3],[3,4]]

    ss = Solution()
    res = ss.findRightInterval(intervals)

    print(res)
