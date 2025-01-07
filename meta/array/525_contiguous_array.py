class Solution:
    def findMaxLength(self, nums):
        """
        This code finds the maximum length of a subarray with an 
        equal number of 0s and 1s by transforming 0 into -1 and computing a running sum.

        It uses a dictionary to store the first occurrence of each 
        running sum so that when the same running sum reappears, 
        the subarray between those indices has net sum zero (equal numbers of 0s and 1s).

        The solution runs in O(n) time and O(n) space, 
        because each element is processed once and we keep a dictionary 
        for running sum indices.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        total_sum = 0

        index_map = dict()
        index_map[0] = -1

        # This will hold the maximum length of the subarray found so far.
        res = 0

        for i, num in enumerate(nums):
            # If the current element is 0, treat it as -1.
            if num == 0:
                total_sum -= 1
            else:  # If the current element is 1, treat it as +1.
                total_sum += 1

            if total_sum in index_map:
                res = max(res, i - index_map[total_sum])
            else:
                index_map[total_sum] = i
        # {0: -1, -1: 0, 1: 4, 2: 7}
        print(index_map)  # Debug print to see final state of index_map, e.g. {0: -1, -1: 0, 1: 4}

        return res


if __name__ == '__main__':

    nums = [0, 1, 0, 1, 1, 0, 1, 1, 0, 1]

    ss = Solution()
    res = ss.findMaxLength(nums)

    print(res) # 6
