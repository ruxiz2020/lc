# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def list_to_binary_tree(lst):
    if not lst:
        return None

    # Create the root of the tree
    root = Node(lst[0])
    queue = [root]  # Queue to hold nodes for assignment
    idx = 1  # Index to traverse the list

    while idx < len(lst):
        # Get the current parent node from the queue
        parent = queue.pop(0)

        # Assign left child if available
        if idx < len(lst) and lst[idx] is not None:
            parent.left = Node(lst[idx])
            queue.append(parent.left)
        idx += 1

        # Assign right child if available
        if idx < len(lst) and lst[idx] is not None:
            parent.right = Node(lst[idx])
            queue.append(parent.right)
        idx += 1

    return root

def print_tree(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    return result

class Solution:
    def connect(self, node: 'Optional[Node]') -> 'Optional[Node]':

        # nxt: start of next row
        cur, nxt = node, node.left if node else None

        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left

            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        return node

lst = [1,2,3,4,5,6,7]

root = list_to_binary_tree(lst)
res = Solution().connect(root)

print_tree(root)
