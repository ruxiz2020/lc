import bisect

class Solution:
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        # base case
        if k == 0: return []
        win = sorted(nums[:k])
        ans = []
        for i in range(k, len(nums)+1):
            median = (win[k//2] + win[(k-1)//2])/2.0
            ans.append(median)
            if i == len(nums):
                break
            # get the index of the nums[i-k] and then delete it, then insort nums[i]
            index = bisect.bisect_left(win, nums[i-k])
            win.pop(index)
            bisect.insort_left(win, nums[i])
            print(i)
            print(win)

        return ans

#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#
import heapq

class HashHeap:
    def __init__(self):
        self.heap = []
        self.deleted = {}       # key (num): value (occurence)
        self._len = 0

    def push(self, val):
        heapq.heappush(self.heap, val)
        self._len += 1

    def pop(self):
        """
        execute lazy removal
        """
        self._clean_top()
        self._len -= 1
        return heapq.heappop(self.heap)

    def remove(self, val):
        self.deleted[val] = self.deleted.get(val, 0) + 1
        self._len -= 1

    def top(self):
        """
        execute lazy removal
        """
        self._clean_top()
        return self.heap[0]

    def _clean_top(self):
        """
        lazy removal
        """
        # if heap top is
        while self.heap and self.deleted.get(self.heap[0]):
            self.deleted[self.heap[0]] -= 1     # update occurence
            heapq.heappop(self.heap)

    def __len__(self):
        return self._len


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        res = []
        n = len(nums)
        if not nums or n < 1 or k <= 0: return res

        self.min_heap = HashHeap()
        self.max_heap = HashHeap()

        for i in range(n):
            # move window
            if i >= k:
                if self.min_heap and nums[i - k] >= self.min_heap.top():
                    self.min_heap.remove(nums[i - k])
                else:
                    self.max_heap.remove(-nums[i - k])

            # load the number
            if self.min_heap and nums[i] > self.min_heap.top():
                self.min_heap.push(nums[i])
            else:
                self.max_heap.push(-nums[i])

            self.balance()

            if i + 1 >= k:
                res.append(self.get_median(k))

        return res

    def balance(self):
        """
        an important thing to notice is the fact that if the two heaps are balanced, only the top of the
        heaps are  actually needed to find the medians. This means that as long as we can somehow keep
        the heaps balanced, we could also keep some extraneous elements.
        """
        l = len(self.max_heap)
        r = len(self.min_heap)
        if abs(r - l) <= 1: return
        if l < r: self.max_heap.push(-self.min_heap.pop())
        else: self.min_heap.push(-self.max_heap.pop())

    def get_median(self, k):
        l = len(self.max_heap)
        r = len(self.min_heap)

        if k % 2 ==0:
            return (-self.max_heap.top() + self.min_heap.top()) / 2.0
        return float(self.min_heap.top() if r > l else -self.max_heap.top())





class Solution(object):
    def medianSlidingWindow(self, nums, k):
        n = len(nums)
        ans = []
        window = sorted(nums[:k])
        if k % 2 != 0:
            ans.append(window[k // 2])
        else:
            ans.append((window[k // 2 - 1] + window[k // 2]) / 2.0)
        p1, p2 = 0, k
        while p2 < n:
            window.remove(nums[p1])
            bisect.insort(window, nums[p2])
            if k % 2 != 0:
                ans.append(window[k // 2])
            else:
                ans.append((window[k // 2 - 1] + window[k // 2]) / 2.0)
            p1 += 1
            p2 += 1
        return ans



import bisect

class Solution(object):
    """O(n * k)"""
    def medianSlidingWindow(self, nums, k): # this solution is just the natural flow
        window = sorted(nums[:k])
        medians = []
        for a, b in zip(nums, nums[k:] + [0]):
        # +[0] to keep the loop running
        # e.g. k=3 and nums[1,2,3], so it should enter the loop for one time
            medians.append((window[k // 2] + window[~(k // 2)]) / 2.)
            window.remove(a)
            bisect.insort(window, b)
        return medians

###########

# heap solution
# Since we are using k-size heap here, the time complexity is O(nlogk)
#   and space complexity is O(logk).
def medianSlidingWindow(nums, k):
	small, large = [], []
	for i, x in enumerate(nums[:k]):
		heapq.heappush(small, (-x,i))
	for _ in range(k-(k>>1)):
		move(small, large)
	ans = [get_med(small, large, k)]
	for i, x in enumerate(nums[k:]):
		if x >= large[0][0]:
			heapq.heappush(large, (x, i+k))
			if nums[i] <= large[0][0]:
				move(large, small)
		else:
			heapq.heappush(small, (-x, i+k))
			if nums[i] >= large[0][0]:
				move(small, large)
		while small and small[0][1] <= i:
			heapq.heappop(small)
		while large and large[0][1] <= i:
			heapq.heappop(large)
		ans.append(get_med(small, large, k))
	return ans

def move(h1, h2):
	x, i = heapq.heappop(h1)
	heapq.heappush(h2, (-x, i))

def get_med(h1, h2, k):
	return h2[0][0] * 1. if k & 1 else (h2[0][0]-h1[0][0]) / 2.




if __name__ == '__main__':

    nums = [1,3,-1,-3,5,3,6,7]
    k = 3

    ss = Solution()
    res = ss.medianSlidingWindow(nums, k)

    print(res)
