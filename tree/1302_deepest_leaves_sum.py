class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = [root]
        while q:
            tmp = []
            for node in q:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if not tmp:
                return sum([n.val for n in q])
            q = tmp
