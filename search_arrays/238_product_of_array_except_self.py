from typing import List

class Solution:
    '''
    O(n)
    O(1)
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


class Solution02:
    '''
    O(n)
    O(1)
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [a * b for a, b in zip(nums, [1] + nums[1:])]
        print(prefix)
        postfix = [a * b for a, b in zip(nums, nums[: -1] + [1])]
        print(postfix)

        return [a * b for a, b in zip(prefix, postfix)]

if __name__ == '__main__':

    nums = [1,2,3,4]

    ss = Solution02()
    res = ss.productExceptSelf(nums)

    print(res)
