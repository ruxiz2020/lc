# Time: O(M+N), M is the size of tree1, N is the size of tree2
# Space: O(M+N)
class Solution:

    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:

        nodes1 = self.in_order(root1)
        nodes2 = self.in_order(root2)

        d = dict()
        for v in nodes1:
            d[target - v] = 1

        for v in nodes2:
            if v in d:
                return True
        return False


    def in_order(self, root):
        if root == None:
            return []
        nodes = []
        cache = []
        while len(cache) > 0 or root:
            while root:
                cache.append(root)
                root = root.left

            root = cache.pop()
            nodes.append(root.val)
            root = root.right
        return nodes



