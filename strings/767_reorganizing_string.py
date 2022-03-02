import collections
import heapq


class Solution:
    def reorganizeString(self, S):
        if not S:
            return ""
        # create a counter
        heap = []
        for key, value in collections.Counter(S).items():
            heapq.heappush(heap, [-value, key])
        #print(heap)
        res = ""
        pre = heapq.heappop(heap)
        res += pre[1]

        while heap:

            curr = heapq.heappop(heap)
            res += curr[1]

            pre[0] += 1
            if pre[0] < 0:
                heapq.heappush(heap, pre)
            pre = curr
            #print(heap)

        print(res)
        return "" if len(res) != len(S) else res

if __name__ == '__main__':

    s = "aaab"

    ss = Solution()
    res = ss.reorganizeString(s)
    print(res)
