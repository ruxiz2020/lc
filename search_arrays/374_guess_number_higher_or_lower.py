# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        # approach: use binary search to prune half candidates per guess

        low = 1
        high= n

        while low <= high:
            mid = low + (high - low) // 2
            result = guess(mid)
            if result > 0:
                low = mid + 1
            elif result < 0:
                high = mid - 1
            else:
                return mid
