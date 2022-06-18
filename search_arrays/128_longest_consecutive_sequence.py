from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    print(n, length)
                    length += 1
                longest = max(length, longest)
        return longest


if __name__ == '__main__':

    nums = [100,4,200,1,3,2]
    ss = Solution()
    res = ss.longestConsecutive(nums)

    print(res)
