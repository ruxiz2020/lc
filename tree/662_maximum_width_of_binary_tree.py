import numpy as np

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def widthOfBinaryTree(self, root):
        q = [(root, 0)]
        res = 1
        while q:
            res = max(res, q[-1][1] - q[0][1] + 1)
            print(q[-1][1], q[0][1])
            tmp = []
            for node, pos in q:
                if node.left:
                    tmp.append((node.left, pos * 2))
                if node.right:
                    tmp.append((node.right, pos * 2 + 1))
            q = tmp
        return res


arr = [1,3,2,5,3,np.nan,9]
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
print("input: " + "arr = [3,1,4,null,2];")


if __name__ == '__main__':


    ss = Solution()
    res = ss.widthOfBinaryTree(root)
    print(res)
