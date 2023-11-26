from typing import List


class Solution:
  def maximalSquare(self, matrix: List[List[chr]]) -> int:
    '''dynamic programmin bottom up
    ercursive: top down
    T: O(m n)
    M: O(m n)'''
    m = len(matrix)
    n = len(matrix[0])
    '''map each (r, c) -> maxLength of the square'''
    cache = {}

    def helper(r, c):
      if r >= m or c >= n:
        return 0

      if (r, c) not in cache:
        down = helper(r + 1, c)
        right = helper(r, c + 1)
        diag = helper(r + 1, c + 1)

        cache[(r, c)] = 0
        if matrix[r][c] == "1":
          cache[(r, c)] = 1 + min(down, right, diag)

      return cache[(r, c)]

    helper(0, 0)
    return max(cache.values()) ** 2
