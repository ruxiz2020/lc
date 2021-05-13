class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        O(logn)
这个问题其实就是求f(x)=num - x ^ 2的零点。

那么，Xn+1 = Xn - f(Xn)/f'(Xn).

又f'(x) = -2x.

得Xn+1 = Xn +(num - Xn ^ 2)/2Xn = (num + Xn ^ 2) / 2Xn = (num / Xn + Xn) / 2.

即t = (num / t + t) / 2.
————————————————
版权声明：本文为CSDN博主「负雪明烛」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/79254648
        """
        num = x
        while num * num > x:
            num = (num + x / num) / 2
        return num


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        O(logn)
        """
        left, right = 0, x + 1
        # [left, right)
        while left < right:
            mid = left + (right - left) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                left = mid + 1
            else:
                right = mid
        return left - 1

x = 4
print("input: x = 4")

ss = Solution()
res = ss.mySqrt(x)
print("res: " + str(res))

x = 8
print("input: x = 8")

ss = Solution()
res = ss.mySqrt(x)
print("res: " + str(res))
