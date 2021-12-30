import collections
import heapq

class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        saved = collections.defaultdict(list)
        for num in nums:

            last = saved[num - 1]
            _len = 0 if (not last) else heapq.heappop(last)
            current = saved[num]
            heapq.heappush(current, _len + 1)
            print(saved)

        for values in saved.values():
            for v in values:
                if v < 3:
                    return False
        return True


if __name__ == '__main__':

    nums = [1,2,3,3,4,5]
    ss = Solution()
    res = ss.isPossible(nums)

    print(res)
