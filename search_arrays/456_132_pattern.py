class Solution(object):

    def find132pattern(self, nums):
        if len(nums) < 3:
            return False
        right = float('-inf')
        stack = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < right:
                return True
            else:
                while stack and stack[-1] < nums[i]:
                    right = stack.pop()
            stack.append(nums[i])
            print(stack)
        return False


if __name__ == '__main__':

    nums = [1,2,3,4]
    ss = Solution()
    res = ss.find132pattern(nums)

    print(res)
