# recursive
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t == None and s == None:
            return True
        if t == None or s == None:
            return False
        if s.val == t.val and self.rootSubtree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def rootSubtree(self, s, t):
        if t == None and s == None:
            return True
        if t == None or s == None or s.val != t.val:
            return False
        return self.rootSubtree(s.left, t.left) and self.rootSubtree(s.right, t.right)


# same as above, but more graceful
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSame(self, s, t):
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False
        if s.val != t.val:
            return False
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
