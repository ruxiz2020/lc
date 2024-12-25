import numpy as np

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def unsorted_array_to_bst(array_nums):

    if len(array_nums) == 0: return None

    root = TreeNode(array_nums[0])

    root.left = unsorted_array_to_bst(array_nums[1:])
    root.right = unsorted_array_to_bst(array_nums[2:])
    return root


def array_to_bst(array_nums):
    if not array_nums:
        return None
    mid_num = len(array_nums) // 2
    node = TreeNode(array_nums[mid_num])
    node.left = array_to_bst(array_nums[:mid_num])
    node.right = array_to_bst(array_nums[mid_num + 1:])
    return node

def print_tree(tree):
    if tree:
        print(tree.val)
        print_tree(tree.left)
        print_tree(tree.right)



class Solution(object):
    """
    O(H)
    O(1)
    """

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        log(n)
        """
        current = root
        while root:

            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                break

        return root


if __name__ == '__main__':
    arr = [6, 2, 8, 0, 4, 7, 9, np.nan, np.nan, 3, 5]
    #root = sortedArrayToBST(sorted(arr))
    root = array_to_bst(arr)
    #print_tree(root)

    p = 2
    pp = TreeNode(p)
    q = 8
    qq = TreeNode(q)

    ss = Solution()
    res = ss.lowestCommonAncestor(root, pp, qq)

    print_tree(res)
