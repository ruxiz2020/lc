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


class Solution(object):
    def find132pattern(self, nums):
        stack = [] # pair
        curMin = nums[0]

        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n > stack[-1][1]:
                return True
            stack.append([n, curMin])
            curMin = min(curMin, n)
        return False

if __name__ == '__main__':

    nums = [1,2,3,4]
    nums = [3,1,4,2]
    ss = Solution()
    res = ss.find132pattern(nums)

    print(res)
