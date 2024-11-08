
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:
    "in order traversal"
    def treeToDoublyList(self, root: 'Node | None') -> 'Node | None':
        if not root:
            return None

        stack = []
        first = None
        pred = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not first:
                first = root
            if pred:
                pred.right = root
                root.left = pred
            pred = root
            root = root.right

        pred.right = first
        first.left = pred
        return first


root = [4,2,5,1,3]

def list_to_binary_tree(lst):
    if not lst or lst[0] is None:
        return None

    # Create the root of the tree
    root = Node(lst[0])
    queue = [root]  # Queue to keep track of nodes to attach children to
    index = 1  # Start from the second element in the list

    while index < len(lst):
        node = queue.pop(0)

        # Add left child
        if index < len(lst) and lst[index] is not None:
            node.left = Node(lst[index])
            queue.append(node.left)

        index += 1  # Move to the next element

        # Add right child
        if index < len(lst) and lst[index] is not None:
            node.right = Node(lst[index])
            queue.append(node.right)

        index += 1  # Move to the next element

    return root

# Convert the list to binary tree
root_list = [4,2,5,1,3]
binary_tree_root = list_to_binary_tree(root_list)

res = Solution().treeToDoublyList(binary_tree_root)
print(res)


