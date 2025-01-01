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
    Convert a BST to a sorted circular doubly linked list.

    In-order traversal ensures nodes are processed in ascending order.
    We maintain a 'prev' pointer to the previously visited node
    and a 'head' pointer to the smallest (first) node in the sequence.

    Time Complexity: O(N), where N is the number of nodes (each visited once).
    Space Complexity: O(H), where H is the height of the tree (for the recursion stack).
      In the worst case (skewed tree), H can be O(N). For a balanced tree, H = O(log N).
    """

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # A helper function to perform in-order DFS traversal and link nodes.
        def dfs(node: 'Optional[Node]'):
            if node is None:
                return  # Base case: nothing to process if the node is None.
            nonlocal prev, head  # Allows access/modification of 'prev' & 'head' defined outside this function.

            # 1. Traverse the left subtree (in-order).
            dfs(node.left)

            # 2. Link the current node with the 'prev' node.
            if prev:
                prev.right = node  # 'prev' node's right pointer goes to the current 'node'.
                node.left = prev   # Current 'node' left pointer goes back to 'prev'.
            else:
                # If 'prev' is None, it means this is the *first* node in in-order traversal.
                head = node  # This node will be the head (smallest) in the doubly-linked list.

            # 3. Update 'prev' to the current node before traversing right subtree.
            prev = node

            # 4. Traverse the right subtree (in-order).
            dfs(node.right)

        # Handle edge case of an empty tree.
        if not root:
            return None

        # 'head' will eventually point to the smallest node (start of the list).
        # 'prev' tracks the previously visited node in the in-order sequence.
        head = prev = None

        # Perform the in-order DFS traversal to link nodes linearly.
        dfs(root)

        # Finally, connect the last node ('prev') with the first node ('head')
        # to make the list circular.
        prev.right = head
        head.left = prev

        # Return the head (start) of the circular doubly linked list.
        return head




# Convert the list to binary tree
root_list = [4, 2, 5, 1, 3]
binary_tree_root = list_to_bst(root_list)

res = Solution().treeToDoublyList(binary_tree_root)
print_forward(res) # 1 <-> 2 <-> 3 <-> 4 <-> 5
