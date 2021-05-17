class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1, p2 = 0, len(nums) - 1
        mid = p1
        while nums[p1] >= nums[p2]:
            if p2 - p1 == 1:
                mid = p2
                break
            mid = (p1 + p2) // 2
            if nums[mid] == nums[p1] and nums[mid] == nums[p2]:
                return self.minInOrder(nums, p1, p2)
            if nums[mid] >= nums[p1]:
                p1 = mid
            elif nums[mid] <= nums[p2]:
                p2 = mid
        return nums[mid]

    def minInOrder(self, nums, index1, index2):
        n1 = nums[index1]
        for i in range(index1 + 1, index2):
            if n1 > nums[i]:
                return nums[i]
        return n1


nums = [2,2,2,0,1]

print("print: " + "nums = [2,2,2,0,1]")

ss = Solution()
res = ss.findMin(nums)

print(res)


nums = [1,3,5]

print("print: " + "nums = [1,3,5]")

ss = Solution()
res = ss.findMin(nums)

print(res)
