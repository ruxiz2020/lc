class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])
        timePoints = list(map(convert, timePoints))
        timePoints.sort()
        return min((y - x) % (24 * 60)  for x, y in zip(timePoints, timePoints[1:] + timePoints[:1]))

if __name__ == '__main__':

    timePoints = ["00:00","23:59","00:00"]

    ss = Solution()
    res = ss.findMinDifference(timePoints)

    print(res)
