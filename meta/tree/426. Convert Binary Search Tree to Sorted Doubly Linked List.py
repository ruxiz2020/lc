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
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(root):
            if root is None:
                return
            nonlocal prev, head
            dfs(root.left)
            if prev:
                prev.right = root
                root.left = prev
            else:
                head = root
            prev = root
            dfs(root.right)

        if root is None:
            return None
        head = prev = None
        dfs(root)
        prev.right = head
        head.left = prev
        return head


# Convert the list to binary tree
root_list = [4, 2, 5, 1, 3]
binary_tree_root = list_to_bst(root_list)

res = Solution().treeToDoublyList(binary_tree_root)
print_forward(res) # 1 <-> 2 <-> 3 <-> 4 <-> 5
