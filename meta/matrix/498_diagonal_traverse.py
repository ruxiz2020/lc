from collections import defaultdict
from typing import List



class Solution:
    """
    O(m * n)
    O(m * n)
    """
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix is None or matrix == []: return []
        res = []
        lines = defaultdict(list)
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                lines[i + j].append(matrix[i][j])
        print(lines) # {0: [1], 1: [2, 4], 2: [3, 5, 7], 3: [6, 8], 4: [9]}
        for k in range(rows + cols - 1):
            if k % 2 == 0:
                res += lines[k][::-1]
            else:
                res += lines[k]
        return res


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
res = Solution().findDiagonalOrder(mat)
print(res) # [1, 2, 4, 7, 5, 3, 6, 8, 9]
