import numpy as np



def array_to_bst(array_nums):
    if not array_nums:
        return None
    mid_num = len(array_nums) // 2
    node = TreeNode(array_nums[mid_num])
    node.left = array_to_bst(array_nums[:mid_num])
    node.right = array_to_bst(array_nums[mid_num + 1:])
    return node


    
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




class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left # go to the left most node
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


arr = [3, 1, 4, np.nan, 2]
k = 1





class Solution:
    def kthSmallest(self, root, k):
        def inorder(root):
            if not root:
                return []
            in_left = inorder(root.left)
            root_val = [root.val]
            in_right = inorder(root.right)
            return in_left + root_val + in_right

        return inorder(root)[k - 1]


if __name__ == '__main__':
    root = array_to_bst(array_nums=sorted(arr))
    print("input: " + "arr = [3,1,4,null,2]; k = 1")

    ss = Solution()
    res = ss.kthSmallest(root, k)
    print(res)
