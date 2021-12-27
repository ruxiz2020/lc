class Solution:
    def searchBST(self, root, val):
        if not root:
            return None
        while root:
            if root.val == val:
                return root
            if root.val > val:
                root = root.left
            else:
                root = root.right


class Solution:
    def searchBST(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)
