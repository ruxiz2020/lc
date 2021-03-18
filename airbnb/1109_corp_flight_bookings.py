class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * n

        for booking in bookings:
            ans[booking[0] - 1] += booking[2]
            if booking[1] < n:
                ans[booking[1]] -= booking[2]

        for i in range(1, n):
            ans[i] += ans[i - 1]

        return ans
