import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            pts.append([dist, x, y])

        res = []
        heapq.heapify(pts) # O(n)
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])
        return res


if __name__ == '__main__':

    points = [[1,3],[-2,2]]
    k = 1

    ss = Solution()
    res = ss.kClosest(points, k)

    print(res)
