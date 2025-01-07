class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode | None):
        self.i = 0
        self.vals = []
        self._inorder(root)

    def next(self) -> int:
        self.i += 1
        return self.vals[self.i - 1]

    def hasNext(self) -> bool:
        return self.i < len(self.vals)

    def _inorder(self, root: TreeNode | None) -> None:
        if not root:
            return
        self._inorder(root.left)
        self.vals.append(root.val)
        self._inorder(root.right)



# Helper function to build a BST from a sorted list
def create_bst(sorted_values):
    """
    Builds a height-balanced BST from a sorted list of values.
    Returns the root of the BST.
    """
    if not sorted_values:
        return None
    mid = len(sorted_values) // 2
    root = TreeNode(sorted_values[mid])
    root.left = create_bst(sorted_values[:mid])
    root.right = create_bst(sorted_values[mid+1:])
    return root

# Test the BSTIterator
if __name__ == "__main__":
    # Create a BST from a sorted list
    values = [1, 2, 3, 4, 5, 6, 7]
    root = create_bst(values)
    
    # Initialize the iterator with the BST root
    iterator = BSTIterator(root)
    
    # Use the iterator to traverse the tree in ascending order
    output = []
    while iterator.hasNext():
        output.append(iterator.next())
    
    # Print the results
    print("BST Inorder Traversal using BSTIterator:", output)
    # Expected output: [1, 2, 3, 4, 5, 6, 7]
