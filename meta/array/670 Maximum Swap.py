

class Solution:
    """
    This code finds the maximum number you can get by swapping 
    two digits of the integer num at most once.

    It traverses the digits from right to left to maintain 
    a stack of rightmost occurrences of larger digits, then moves from 
    left to right to find the first digit that can be increased by 
    swapping with one of those larger digits on the right.

    The algorithm runs in O(n) time and uses O(n) space for the stack, where 
    n is the number of digits in num.
    O(n)
    O(N)
    """
    def maximumSwap(self, num: int) -> int:
        """
        stk maintain a increasing stack from right to left
        """
        stk = []
        nums = list(str(num))
        n = len(nums)
        for i in range(n - 1, -1, -1):  # find the largest num from the right
            if stk and stk[-1][1] >= nums[i]:   
                continue
            stk.append((i, nums[i]))
        print(stk)  # [(3, '3'), (2, '7'), (1, '9')]

        for i in range(n):
            while stk and stk[-1][0] <= i:
                stk.pop()
            if stk and stk[-1][1] > nums[i]:
                j = stk[-1][0]
                nums[i], nums[j] = nums[j], nums[i]
                break

        return int("".join(nums))


if __name__ == "__main__":
    assert Solution().maximumSwap(2736) == 7236
    assert Solution().maximumSwap(9973) == 9973
