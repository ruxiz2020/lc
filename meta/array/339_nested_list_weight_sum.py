

class Solution(object):
    """
    O(N)
    O(D)
    """
    def depthSum(self, nestedList):
        def DFS(nestedList, depth):
            temp_sum = 0
            for elem in nestedList:
                if type(elem) == int:
                    temp_sum += elem * depth
                else:
                    temp_sum += DFS(elem, depth + 1)
            return temp_sum
        return DFS(nestedList, 1)


if __name__ == '__main__':

    nestedList = [[1,1],2,[1,1]]

    ss = Solution()
    res = ss.depthSum(nestedList)

    print(res)
    # 10
