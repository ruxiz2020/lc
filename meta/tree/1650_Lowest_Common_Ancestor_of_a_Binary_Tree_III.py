class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    """
    Time Complexity: O(H)
        Where H is the height of the tree (or the maximum distance up to the root).
        In the worst case, both pointers might travel all the way up to the root.

    Space Complexity: O(1)
        We only use a couple of references and do not allocate extra data structures.

    This approach is analogous to "Linked List Intersection" (LeetCode #160)
    but adapted for trees using parent pointers.
    """

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Returns the Lowest Common Ancestor (LCA) of two nodes p and q in a tree
        where each node has a pointer to its parent.

        The trick (like the linked list intersection problem) is that we use two pointers
        (a and b) and move them up the tree. When one pointer reaches the root (None for
        parent), it is reassigned to the other node. Eventually, they meet at the LCA.
        """

        # a and b will traverse upwards from p and q, respectively.
        a = p
        b = q

        # Continue traversing until a and b point to the same node (the LCA),
        # or both become None (in case p and q are not in the same tree).
        while a != b:
            # If 'a' is not None, move a one step up (a's parent).
            # Otherwise, if a is None, reset it to 'q'.
            # This mimics the approach in "Intersection of Two Linked Lists".
            a = a.parent if a else q

            # Similarly for b: move up if possible, otherwise reset to 'p'.
            b = b.parent if b else p

        # When they meet, that node is the LCA.
        return a


# -----------------------------
# TEST CODE
# -----------------------------
def build_sample_tree():
    """
    Build a small example tree (not necessarily binary) with parent pointers.

        (root, val=1)
        /         \
       2           3
      / \         / \
     4   5       6   7
        /
       8

    Returns the nodes so we can pick p and q for testing.
    """

    root = Node(1)
    node2 = Node(2, parent=root)
    node3 = Node(3, parent=root)
    node4 = Node(4, parent=node2)
    node5 = Node(5, parent=node2)
    node6 = Node(6, parent=node3)
    node7 = Node(7, parent=node3)
    node8 = Node(8, parent=node5)

    # Connect root's children (not necessary for this LCA approach,
    # but might be helpful if you want a fully connected tree).
    # Since we only use parent pointers, child pointers are optional.
    # root.left = node2
    # root.right = node3
    # node2.left = node4
    # node2.right = node5
    # node3.left = node6
    # node3.right = node7
    # node5.left = node8

    # Return a dictionary of nodes for easy access
    return {
        "root": root,
        "node2": node2,
        "node3": node3,
        "node4": node4,
        "node5": node5,
        "node6": node6,
        "node7": node7,
        "node8": node8
    }

if __name__ == "__main__":
    # Build the sample tree
    nodes = build_sample_tree()
    root = nodes["root"]
    node2 = nodes["node2"]
    node3 = nodes["node3"]
    node4 = nodes["node4"]
    node5 = nodes["node5"]
    node6 = nodes["node6"]
    node7 = nodes["node7"]
    node8 = nodes["node8"]

    # Create a solution instance
    sol = Solution()

    # Test 1: LCA of node4 and node5 should be node2
    lca1 = sol.lowestCommonAncestor(node4, node5)
    print(f"LCA of {node4.val} and {node5.val} is {lca1.val if lca1 else None}")

    # Test 2: LCA of node4 and node8 should be node2
    lca2 = sol.lowestCommonAncestor(node4, node8)
    print(f"LCA of {node4.val} and {node8.val} is {lca2.val if lca2 else None}")

    # Test 3: LCA of node8 and node6 should be root (val=1)
    lca3 = sol.lowestCommonAncestor(node8, node6)
    print(f"LCA of {node8.val} and {node6.val} is {lca3.val if lca3 else None}")

    # Test 4: LCA of node6 and node7 should be node3
    lca4 = sol.lowestCommonAncestor(node6, node7)
    print(f"LCA of {node6.val} and {node7.val} is {lca4.val if lca4 else None}")
