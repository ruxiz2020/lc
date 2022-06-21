from typing import List
import itertools

class Solution:
  def largestTimeFromDigits(self, A: List[int]) -> str:
    for time in itertools.permutations(sorted(A, reverse=True)):
      if time[:2] < (2, 4) and time[2] < 6:
        return '%d%d:%d%d' % time

    return ''




if __name__ == '__main__':

    arr = [1,2,3,4]
    print(list(itertools.permutations(sorted(arr, reverse=True))))

    ss = Solution()
    res = ss.largestTimeFromDigits(arr)

    print(res)
