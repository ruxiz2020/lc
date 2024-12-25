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
    O(N)
    O(H)
    """
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # Initialize a variable to store the maximum diameter found during traversal.
        ans = 0

        # Helper function to calculate the maximum depth of a subtree.
        # This function will also calculate the diameter as a side effect.
        def maxDepth(root: TreeNode) -> int:
            nonlocal ans  # Use the `ans` variable from the outer scope to store the diameter.

            # Base case: If the node is None (leaf node's child), its depth is 0.
            if not root:
                return 0

            # Recursively calculate the maximum depth of the left subtree.
            l = maxDepth(root.left)

            # Recursively calculate the maximum depth of the right subtree.
            r = maxDepth(root.right)

            # Update the diameter at the current node.
            # Diameter at the current node = sum of the depths of the left and right subtrees.
            ans = max(ans, l + r)

            # Return the maximum depth of the subtree rooted at the current node.
            # Add 1 to include the current node itself.
            return 1 + max(l, r)

        # Start the recursion from the root to calculate the diameter.
        maxDepth(root)

        # Return the maximum diameter found.
        return ans



lst = [1,2,3,4,5]
root = list_to_binary_tree(lst)
res = Solution().diameterOfBinaryTree(root)

print(res) #3
