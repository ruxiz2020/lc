class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        greedy
        """
        reach = 0
        for i, num in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + num)
        return True

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

        
if __name__ == '__main__':

    nums = [2,3,1,1,4]

    ss = Solution()
    res = ss.canJump(nums)

    print(res)
