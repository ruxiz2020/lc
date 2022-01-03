class Solution:
    def employeeFreeTime(self, schedule):
        if not schedule:
            return []

        intervals = sorted([i for s in schedule for i in s], key=lambda x: x[0])
        res, prev = [], intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= prev[-1]:
                prev[-1] = max(prev[-1], interval[-1])
            else:
                res.append([prev[-1], interval[0]])
                prev = interval
        return res


if __name__ == '__main__':

    schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]

    ss = Solution()
    res = ss.employeeFreeTime(schedule)

    print(res)
