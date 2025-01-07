import math
from typing import List


class Solution:
    """
    This code finds the minimum eating speed 
k such that Koko can eat all the banana piles within 
h hours by performing a binary search over possible eating speeds, where 
k ranges from 1 to the maximum pile size.

The helper function can_eat_all(k) checks if all piles can be eaten within 
h hours at speed 
k by summing the ceiling of the division of each pile size by 
k, ensuring 
O(n) time per check.
    O(N * log M)
    O(1)
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all(k):
            return sum(math.ceil(pile / k) for pile in piles) <= h # O(n)

        low, high = 1, max(piles)
        # O(log M)
        while low < high:
            mid = (low + high) // 2
            print(mid)
            if can_eat_all(mid):
                print("can eat all")
                high = mid
            else:
                low = mid + 1
        return low

piles = [3, 6, 7, 11];
h = 8
res = Solution().minEatingSpeed(piles, h)
print(res) # 4
