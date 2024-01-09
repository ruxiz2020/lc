from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
            m = len(mat)
            n = len(mat[0])
            d = m + n - 3
            O(m * n) space O(d * min(m, n) * log(min(m, n))) time
        """
        def diagonals(mat: List[List[int]]):
            m, n = len(mat), len(mat[0])
            for d in range(2 - m, n - 1):
                print(m, n, d)
                print(range(-min(0, d), m), range(max(0, d), n))
                print(list(zip(range(-min(0, d), m), range(max(0, d), n))))
                yield list(zip(range(-min(0, d), m), range(max(0, d), n)))
        for diagonal in diagonals(mat):
            #print(diagonal)
            dsorted = sorted([mat[r][c] for r, c in diagonal])
            for r, c in diagonal:
                mat[r][c] = dsorted.pop(0)
        return mat

if __name__ == '__main__':

    mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]

    #mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]

    #mat = [[37,98,82,45,42]]
    ss = Solution()
    res = ss.diagonalSort(mat)

    print(mat)
