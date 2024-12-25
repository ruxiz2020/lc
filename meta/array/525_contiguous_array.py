class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        This function returns the length of the longest contiguous subarray
        containing an equal number of 0's and 1's.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        print(nums)  # Debug print to see the input array

        # total_sum will be our running 'balance' or cumulative sum.
        # We treat 0 as -1 and 1 as +1.
        total_sum = 0

        # index_map will map a cumulative sum to the earliest index
        # at which this sum is seen.
        # We initialize index_map with 0 -> -1 because having a sum of 0
        # at index -1 helps when a valid subarray starts from index 0.
        index_map = dict()
        index_map[0] = -1

        # This will hold the maximum length of the subarray found so far.
        res = 0

        # Iterate over each element with its index in the list.
        for i, num in enumerate(nums):
            # If the current element is 0, treat it as -1.
            if num == 0:
                total_sum -= 1
            else:  # If the current element is 1, treat it as +1.
                total_sum += 1

            # If total_sum is seen before, a subarray with sum = 0
            # has been found (from index_map[total_sum] + 1 to i).
            if total_sum in index_map:
                # Calculate the length of this subarray and compare with max length.
                res = max(res, i - index_map[total_sum])
            else:
                # Otherwise, record the first time we see this sum with index i.
                index_map[total_sum] = i

        print(index_map)  # Debug print to see final state of index_map, e.g. {0: -1, -1: 0, 1: 4}

        return res


if __name__ == '__main__':

    nums = [0, 1, 0, 1, 1, 0, 1, 1, 0, 1]

    ss = Solution()
    res = ss.findMaxLength(nums)

    print(res) # 6
