class Solution(object):
    def sortArrayByParityII(self, A):
        odd, even = 1 , 0
        size = len(A)

        while odd < size and even < size:
            while odd < size and A[odd] % 2 == 1:
                odd += 2
            while even < size and A[even] % 2 == 0:
                even += 2
            if odd < size and even < size:
                A[odd], A[even] = A[even], A[odd]
                odd += 2 ; even += 2  # Optional Line
        return A
