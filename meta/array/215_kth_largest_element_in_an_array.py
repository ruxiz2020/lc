import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        n + k(log n)
        """
        heapq.heapify(nums)
        n = len(nums)
        while n > k:
            heapq.heappop(nums)
            n -= 1
        return nums[0]


class Solution2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        O(n)
        """
        k = len(nums) - k
        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                print(f"i: {i}")
                if nums[i] <= pivot:
                    print(f"p: {p}")
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k: return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else: return nums[p]

        return quickSelect(0, len(nums) - 1)


class Solution3(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        quick select
        avg: O(n)
        worst: O(n * n)
        """
        def partition(arr, l, r):

            pivot = arr[r]
            i = l
            for j in range(l, r):
                print(f"j:{j}")
                if arr[j] <= pivot:
                    print(f"i:{i}")
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1

            arr[i], arr[r] = arr[r], arr[i]
            return i

        def kthSmallest(arr, l, r, k):

            # if k is smaller than number of
            # elements in array
            if (k > 0 and k <= r - l + 1):

                # Partition the array around last
                # element and get position of pivot
                # element in sorted array
                index = partition(arr, l, r)

                # if position is same as k
                if (index - l == k - 1):
                    return arr[index]

                # If position is more, recur
                # for left subarray
                if (index - l > k - 1):
                    return kthSmallest(arr, l, index - 1, k)

                # Else recur for right subarray
                return kthSmallest(arr, index + 1, r,
                            k - index + l - 1)
            return int(float('inf'))

        n, k = len(nums), len(nums) - k + 1
        low, high = 0, n - 1

        res = kthSmallest(nums, low, high, k)

        return res

nums = [3,2,1,5,6,4]
k = 2
ss = Solution()
res = ss.findKthLargest(nums, k)
print(res)
