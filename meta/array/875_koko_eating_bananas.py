import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r = 1, max(piles)
        k = 0

        while l <= r:
            m = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= H:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k
