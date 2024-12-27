# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_binary_tree(lst):
    if not lst or lst[0] is None:
        return None

    # Create the root of the tree
    root = TreeNode(lst[0])
    queue = [root]  # Queue to keep track of nodes to attach children to
    index = 1  # Start from the second element in the list

    while index < len(lst):
        node = queue.pop(0)

        # Add left child
        if index < len(lst) and lst[index] is not None:
            node.left = TreeNode(lst[index])
            queue.append(node.left)

        index += 1  # Move to the next element

        # Add right child
        if index < len(lst) and lst[index] is not None:
            node.right = TreeNode(lst[index])
            queue.append(node.right)

        index += 1  # Move to the next element

    return root



class Solution:
    """
    Computes the diameter of a binary tree.
    The diameter is the length of the longest path between any two nodes in the tree.

    Time Complexity: O(N)
      - We perform a single DFS traversal, visiting each node once.
    Space Complexity: O(H), where H is the height of the tree
      - due to the recursion call stack. In the worst case of a skewed tree, H = N.

    """
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 'ans' will track the maximum diameter seen so far.
        ans = 0

        def maxDepth(node: TreeNode) -> int:
            """
            Returns the maximum depth of the subtree rooted at 'node'.
            Also updates 'ans' to reflect the largest diameter encountered.
            """
            nonlocal ans  # Allows us to update 'ans' in this nested function

            # Base case: if there's no node, the depth is 0, and no path extends here.
            if not node:
                return 0

            # Recurse into left subtree to find its maximum depth
            left_depth = maxDepth(node.left)
            # Recurse into right subtree to find its maximum depth
            right_depth = maxDepth(node.right)

            # Diameter through this node is the sum of left and right depths
            # Compare with the global 'ans' and update if larger
            ans = max(ans, left_depth + right_depth)

            # Return the maximum depth at this node: 1 (itself) plus the max of left/right
            return 1 + max(left_depth, right_depth)

        # Perform the DFS from the root, which will also compute 'ans'
        maxDepth(root)

        # 'ans' now holds the diameter of the binary tree
        return ans




lst = [1,2,3,4,5]
root = list_to_binary_tree(lst)
res = Solution().diameterOfBinaryTree(root)

print(res) #3
