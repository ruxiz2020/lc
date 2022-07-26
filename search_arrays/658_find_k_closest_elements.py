class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        while len(arr) > k:
            if x - arr[0] <= arr[-1] - x:
                arr.pop()
            else:
                arr.pop(0)
        return arr


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l, r = 0, len(arr) - k

        while l < r:
            m = (1 + r) // 2
            if x - arr[m] <= arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l, l+k]


if __name__ == '__main__':

    arr = [1,2,3,4,5]
    k = 4
    x = 3
    ss = Solution()
    res = ss.findClosestElements(arr, k, x)

    print(res)
