import collections
import heapq


class Solution:
    def reorganizeString(self, S):
        count = collections.Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap) # O(n)

        prev = None
        res = ""
        while maxHeap or prev:
            print(maxHeap, prev)
            if prev and not maxHeap:
                return ""
            # most frequent except prev
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1 # negative cnt

            if prev:
                print(1)
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                print(2)
                prev = [cnt, char]
        return res


if __name__ == '__main__':

    s = "aaabca"

    ss = Solution()
    res = ss.reorganizeString(s)
    print(res)
