import collections, heapq

from typing import List


class Solution01(object):

    def topKFrequent(self, nums, k):
        '''klogn'''
        res=[]
        dict = collections.Counter(nums)
        for val, count in dict.items():
            if len(res)<k:
                heapq.heappush(res,(count,val))
            else:
                heapq.heappush(res,(count,val))
                heapq.heappop(res)
        for c, v in res:
            print(c, v)
        return [val for count, val in res]


from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums).most_common()
        return [counter[i][0] for i in range(k)]

class Solution02:
    '''bucket sort'''
    # O(n)
    #
    def topKFrequent(self, nums: List, k: int) -> List:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        print(freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            print(i)
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


if __name__ == '__main__':

    nums = [1,1,1,2,2,3]; k = 2

    ss = Solution02()
    res = ss.topKFrequent(nums, k)

    print(res)
    # [1, 2]
