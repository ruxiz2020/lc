from typing import List


class SparseVector:
    """
    O(min(k1, k2))
    O(1)
    """
    def __init__(self, nums: List[int]):
        self.d = {i: v for i, v in enumerate(nums) if v}
        print(self.d)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        a, b = self.d, vec.d
        if len(b) < len(a):
            a, b = b, a
        return sum(v * b.get(i, 0) for i, v in a.items())


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

nums1 = [1,0,0,2,3]; # {0: 1, 3: 2, 4: 3}
nums2 = [0,3,0,4,0] # {1: 3, 3: 4}
v1 = SparseVector(nums1)
res = v1.dotProduct(SparseVector(nums2))
print(res)
