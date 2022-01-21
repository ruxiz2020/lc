import collections, heapq

class Solution(object):

    def topKFrequent(self, nums, k):
        res=[]
        dict = collections.Counter(nums)
        for val, count in dict.items():
            if len(res)<k:
                heapq.heappush(res,(count,val))
            else:
                heapq.heappush(res,(count,val))
                heapq.heappop(res)
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


if __name__ == '__main__':

    nums = [1,1,1,2,2,3]; k = 2

    ss = Solution()
    res = ss.topKFrequent(nums, k)

    print(res)
