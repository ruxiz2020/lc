class Solution:
    """

    O (log ^2 n)
    """
    def divide(self, dividend: int, divisor: int) -> int:
        # -2^{31} / -1 = 2^31 will overflow, so return 2^31 - 1.
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        ans = 0
        dvd = abs(dividend)
        dvs = abs(divisor)

        while dvd >= dvs:
            k = 1
            while k * 2 * dvs <= dvd:
                k <<= 1
            dvd -= k * dvs
            ans += k

        return sign * ans



class Solution:
    def divide(self, A: int, B: int) -> int:
        if A == -2147483648 and B == -1: return 2147483647
        ans, sign = 0, 1
        if A < 0: A, sign = -A, -sign
        if B < 0: B, sign = -B, -sign
        if A == B: return sign
        while A >= B:
            b = 0
            while B << b <= A: b += 1
            A -= B << b - 1
            ans += 1 << b - 1
        return -ans if sign < 0 else ans

dividend = 10; divisor = 3

ss = Solution()
res = ss.divide(dividend, divisor)
print(res)
