class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O (n)
        """
        print(nums)
        total_sum = 0
        index_map = dict()
        index_map[0] = -1
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                total_sum -= 1
            else:
                total_sum += 1
            if total_sum in index_map:
                res = max(res, i - index_map[total_sum])
            else:
                index_map[total_sum] = i
        print(index_map) # {0: -1, -1: 0, 1: 4}
        return res

if __name__ == '__main__':

    nums = [0, 1, 0, 1, 1, 0, 1, 1, 0, 1]

    ss = Solution()
    res = ss.findMaxLength(nums)

    print(res) # 6
