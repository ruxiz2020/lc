# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def get_height(root):
            return 1 + get_height(root.left) if root else -1

        res = 0
        h = get_height(root)
        if h < 0:
            return 0
        while root:
            if get_height(root.right) == h - 1:
                print(res, h)
                res += 1 << h
                print(res)
                root = root.right
            else:
                res += 1 << (h - 1)
                #print(res)
                root = root.left
            h -= 1
        return res


if __name__ == '__main__':

    array_nums = [1,2,3,4,5,6]

    def array_to_bst(array_nums):
        if not array_nums:
            return None
        mid_num = len(array_nums) // 2
        node = TreeNode(array_nums[mid_num])
        node.left = array_to_bst(array_nums[:mid_num])
        node.right = array_to_bst(array_nums[mid_num + 1:])
        return node

    root = array_to_bst(array_nums)


    ss = Solution()
    res = ss.countNodes(root)

    print(res)
