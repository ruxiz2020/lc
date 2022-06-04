class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n == 0:
            return [newInterval]
        res = []
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        #print(res)
        l, r = newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            print(i)
            l = min(l, intervals[i][0])
            r = max(r, intervals[i][1])

            i += 1
            print(l, r)
        res.append([l, r])
        res.extend(intervals[i:])
        return res


if __name__ == '__main__':

    intervals = [[1,3],[6,9]]
    newInterval = [2,5]

    ss = Solution()
    res = ss.insert(intervals, newInterval)

    print(res)
