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
    O(H) time complexity where H is the height of the tree.
    O(1) space complexity.
    """
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        current = root  # Start traversal from the root node
        while current:
            # If both p and q are smaller than current, go left
            if current.val > p.val and current.val > q.val:
                current = current.left
            # If both p and q are larger than current, go right
            elif current.val < p.val and current.val < q.val:
                current = current.right
            # Found the split point (current is between p and q)
            else:
                return current



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
