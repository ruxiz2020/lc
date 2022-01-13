class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float

        not working
        """
        N = len(stations)
        left = 0
        right = stations[N - 1] - stations[0];

        while (right - left > 1e-6):
            mid = (left + right) // 2;
            count = 0;
            for i in range(len(stations) - 1):
                count += ((stations[i + 1] - stations[i]) // mid) - 1;
            if (count > K):
                left = mid;
            else:	#变小加油站距离
                right = mid;

        return right;


if __name__ == '__main__':

    stations = [23,24,36,39,46,56,57,65,84,98]; k = 1

    ss = Solution()
    res = ss.minmaxGasDist(stations, k)

    print(res)
