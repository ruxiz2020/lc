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


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in intervals:
            start, end = i.start, i.end
            time.append((start, 1))
            time.append((end, -1))

        time.sort(key=lambda x: (x[0], x[1]))

        count = 0
        max_count = 0
        for t in time:
            count += t[1]
            max_count = max(max_count, count)
        return max_count


if __name__ == '__main__':

    intervals = [(0,30),(5,10),(15,20)]

    ss = Solution()
    res = ss.minMeetingRooms(intervals)

    print(res)
