import collections, heapq

class Solution:
    def frequencySort(self, s):
        heap = []
        for v, c in collections.Counter(s).items():
            heapq.heappush(heap,[-c,v])
        print(heap)
        res = ""
        while heap:
            c, v = heapq.heappop(heap)
            res += v*-c
        return res


if __name__ == '__main__':

    s = "tree"

    ss = Solution()
    res = ss.frequencySort(s)
    print(res)
