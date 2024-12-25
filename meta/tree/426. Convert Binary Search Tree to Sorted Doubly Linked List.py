def insert_into_bst(root, value):
    if not root:
        return Node(value)
    if value < root.val:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root


def list_to_bst(lst):
    if not lst:
        return None
    root = Node(lst[0])  # The first element is the root
    for value in lst[1:]:
        insert_into_bst(root, value)  # Insert each remaining element into the BST
    return root

# Function to print the list forward
def print_forward(head):
    print("Doubly Linked List (Forward): ", end="")
    current = head
    visited = set()  # Keep track of visited nodes to avoid infinite loops
    while current:
        if current in visited:  # Detect cycles
            print("[Cycle Detected]")
            break
        visited.add(current)
        print(current.val, end=" <-> " if current.right else "")
        current = current.right

    print()

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    O(N)
    O(H)
    """
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Helper function to perform in-order DFS traversal and link nodes.
        def dfs(root):
            if root is None:
                # Base case: If the node is None, there's nothing to process.
                return
            nonlocal prev, head  # Use `prev` and `head` from the outer scope.

            # Recursively process the left subtree.
            dfs(root.left)

            # If `prev` exists, link the previous node to the current node.
            if prev:
                prev.right = root  # Set the right pointer of the previous node to the current node.
                root.left = prev   # Set the left pointer of the current node to the previous node.
            else:
                # If `prev` is None, this is the first node in in-order traversal.
                # Set `head` to the current node (smallest value in the BST).
                head = root

            # Update `prev` to the current node before moving to the right subtree.
            prev = root

            # Recursively process the right subtree.
            dfs(root.right)

        # Edge case: If the root is None, return None (empty tree).
        if root is None:
            return None

        # Initialize `head` (start of the linked list) and `prev` (previous node).
        head = prev = None

        # Perform in-order traversal and link nodes to form the doubly linked list.
        dfs(root)

        # After traversal, link the last node (`prev`) with the first node (`head`)
        # to make the linked list circular.
        prev.right = head
        head.left = prev

        # Return the head of the doubly linked list.
        return head



# Convert the list to binary tree
root_list = [4, 2, 5, 1, 3]
binary_tree_root = list_to_bst(root_list)

res = Solution().treeToDoublyList(binary_tree_root)
print_forward(res) # 1 <-> 2 <-> 3 <-> 4 <-> 5
