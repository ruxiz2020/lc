#this is the solution of Question 528 on Leetcode
#O(log(n)) time complexity for each pickIndex operation, O(n) space complexity


# we need to do a weighted random selection and probability of each element increases with its value
# we can do a prefix sum and choose a random number between 0 and last number in array.
# then we'll do a binary search to find the index of that number.
# if ith element is large, after prefix sum, arr[i] - arr[i-1] will be large and probability of selecting a random
# int between arr[i-1] and arr[i] will increase


import random
from bisect import bisect_left
from typing import List

class Solution:
    """
    This class allows picking an index from the given list of weights (w)
    such that the probability of picking an index i is proportional to w[i].

    Time Complexity of pickIndex: O(log(n))
    because we use binary search on the prefix sums array.
    """

    def __init__(self, w: List[int]):
        self.w = w
        # Convert the list of weights into a prefix sum array.
        # For example, if w = [1, 3, 5, 10],
        # after this loop, self.w = [1, 4, 9, 19].
        # This means:
        #   - [0..0] sum = 1
        #   - [0..1] sum = 4
        #   - [0..2] sum = 9
        #   - [0..3] sum = 19
        for i in range(1, len(w)):
            self.w[i] += self.w[i - 1]

        print(self.w)  # Debug: see the resulting prefix sums, e.g. [1, 4, 9, 19]

    def pickIndex(self) -> int:
        """
        Randomly pick an index in proportion to its weight.

        1. Generate a random integer between 1 and self.w[-1] (inclusive).
           This random value is effectively our 'target' in the prefix sum range.
        2. Use binary search (bisect_left) to find the lowest index
           whose prefix sum is >= target. That index is returned.
        """
        # 1) Generate a random integer in [1, total_sum_of_weights].
        value = random.randint(1, self.w[-1])

        # 2) Use bisect_left to do a binary search over the prefix sum array.
        #    This finds the leftmost position where 'value' can be inserted
        #    to maintain sorted order. Effectively, it tells us which bucket
        #    or index is 'hit' by the random number.
        return bisect_left(self.w, value)



ss = Solution([1, 3, 5, 10])
res = ss.pickIndex()
print(res) # 2 / 3

