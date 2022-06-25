import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # sort the intervals by start time
        intervals.sort(key = lambda x: x[0])
        heap = []
        for interval in intervals:
            if heap and interval[0] >= heap[0]:
                # room is already used in last meeting and continue to use the same room for this meeting
                heapq.heapreplace(heap, interval[-1])
                print(heap)
            else:
                heapq.heappush(heap, interval[-1])

        return len(heap)


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res


if __name__ == '__main__':

    intervals = [(0,30),(5,10),(15,20)]

    ss = Solution()
    res = ss.minMeetingRooms(intervals)

    print(res)
