class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        print(num)
        if num <= 0: return False
        if num == 1: return True
        if num % 4 == 0:
            return self.isPowerOfFour(num / 4)
        return False


if __name__ == '__main__':

    num = 24

    ss = Solution()
    res = ss.isPowerOfFour(num)

    print(res)
