class Solution:
    def intervalIntersection(self, A, B):
        i, j, res = 0, 0, []
        while i < len(A) and j < len(B):

            start, end = max(A[i][0], B[j][0]), min(A[i][1], B[j][1])
            if start <= end:
                res.append([start, end])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res


if __name__ == '__main__':

    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]

    ss = Solution()
    res = ss.intervalIntersection(firstList, secondList)

    print(res)
