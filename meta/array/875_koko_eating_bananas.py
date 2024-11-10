import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all(k):
            return sum(math.ceil(pile / k) for pile in piles) <= h

        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if can_eat_all(mid):
                high = mid
            else:
                low = mid + 1
        return low

piles = [3, 6, 7, 11];
h = 8
res = Solution().minEatingSpeed(piles, h)
print(res)
