class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        m log(sum_)
        """
        n = len(nums)

        start = max(nums)
        end = sum(nums)

        while start + 1 < end:
            mid = start + (end - start) // 2

            if self.split_into_pieces(nums, mid) > m:
                start = mid + 1
            else:
                end = mid

        if self.split_into_pieces(nums, start) <= m:
            return start

        return end

    def split_into_pieces(self, nums, largest_sum):

        previous_sum = 0
        pieces = 1

        for num in nums:
            if previous_sum + num > largest_sum:
                previous_sum = num
                pieces += 1
            else:
                previous_sum += num

        return pieces
