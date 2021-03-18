class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        grays = dict()
        grays[0] = ['0']
        grays[1] = ['0', '1']
        for i in range(2, n + 1):
            n_gray = []
            for pre in grays[i - 1]:
                n_gray.append('0' + pre)
            for pre in grays[i - 1][::-1]:
                n_gray.append('1' + pre)
            grays[i] = n_gray
        return map(lambda x: int(x, 2), grays[n])
