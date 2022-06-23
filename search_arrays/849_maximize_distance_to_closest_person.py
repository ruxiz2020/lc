import itertools
from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        count_dups = [sum(1 for _ in group) for _, group in itertools.groupby(seats)]
        odds = count_dups[0::2]
        evens = count_dups[1::2]
        if seats[0] == 0:
            zeros = max(odds)
            indexes = [i for i, e in enumerate(odds) if e == zeros]
            indexes = [i * 2 for i in indexes]
        else:
            zeros = max(evens)
            indexes = [i for i, e in enumerate(evens) if e == zeros]
            print(indexes)
            indexes = [i + 2**i for i in indexes]

        #print(zeros)
            print(indexes)
        #print(count_dups)
        if 0 in indexes or (len(count_dups) - 1) in indexes:
            res = zeros
        else:
            res = (zeros + 1) // 2
        #print(res)
        return res



if __name__ == '__main__':

    seats = [1,0,0,0]


    ss = Solution()
    res = ss.maxDistToClosest(seats)

    print(res)
