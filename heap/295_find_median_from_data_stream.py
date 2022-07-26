import heapq
class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, min-heap with invert values
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
print(mf.small, mf.large)
mf.addNum(3)
print(mf.small, mf.large)
mf.addNum(4)
print(mf.small, mf.large)
mf.addNum(5)
print(mf.small, mf.large)
print(mf.findMedian())
