import numpy as np

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归


class Solution:
    def kthSmallest(self, root, k):
        def inorder(root):
            if not root:
                return
            res = inorder(root.left)
            if res is not None:
                return res
            self.k -= 1
            if self.k == 0:
                return root.val
            else:
                return inorder(root.right)

        self.k = k
        return inorder(root)


arr = [3, 1, 4, np.nan, 2]
k = 1


def array_to_bst(array_nums):
    if not array_nums:
        return None
    mid_num = len(array_nums) // 2
    node = TreeNode(array_nums[mid_num])
    node.left = array_to_bst(array_nums[:mid_num])
    node.right = array_to_bst(array_nums[mid_num + 1:])
    return node


root = array_to_bst(array_nums=sorted(arr))
print("input: " + "arr = [3,1,4,null,2]; k = 1")

ss = Solution()
res = ss.kthSmallest(root, k)
print(res)
