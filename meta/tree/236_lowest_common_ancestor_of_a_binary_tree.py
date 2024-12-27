class Solution(object):
    """
    We use a simple top-down recursive approach.

    - If the current root is None, return None.
    - If the current root is p or q, return root.
    - Otherwise, recursively check left and right subtrees.
      - If both left and right subtrees return non-null,
        it means p and q lie in different branches,
        so current root is the LCA.
      - If exactly one side returns non-null, that side
        contains both p and q, so return that side's result.

    Time Complexity: O(N), where N is the number of nodes in the tree,
      since in the worst case we might visit all nodes.
    Space Complexity: O(H), where H is the height of the tree,
      corresponding to the max depth of the recursion stack.
    """
    def lowestCommonAncestor(self, root, p, q):
        # If there's no node, there's no LCA to find.
        if not root:
            return None

        # If this node is either p or q, return it immediately.
        # This acts as a found marker.
        if root == p or root == q:
            return root

        # Recursively search for p and q in the left and right subtrees.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-null, p and q are in different subtrees,
        # so root is their common ancestor.
        if left and right:
            return root

        # Otherwise, if only one side is non-null, return that side
        # (which implies both p and q are found in that subtree).
        return left if left else right

