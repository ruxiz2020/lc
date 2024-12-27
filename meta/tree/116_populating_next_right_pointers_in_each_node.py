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
    """
    Time Complexity: O(N), where N is the total number of nodes in the tree.
    Space Complexity: O(1), we use constant extra space (pointers only).
    """
    def connect(self, node: 'Optional[Node]') -> 'Optional[Node]':
        """
        Given a perfect binary tree, populate each node's next pointer to
        point to its next right node (or None if it is the rightmost node).
        """

        # cur: pointer to the current node in the current level
        # nxt: pointer to the first node (leftmost) in the next level
        cur, nxt = node, node.left if node else None

        # Continue until we run out of levels (nxt = None means no further level)
        while cur and nxt:
            # Connect the left child to the right child
            cur.left.next = cur.right

            # If there's a next sibling, connect current node's right child
            # to the sibling's left child
            if cur.next:
                cur.right.next = cur.next.left

            # Move to the next sibling in the same level
            cur = cur.next

            # If we've reached the end of the current level (cur == None),
            # move down to the next level
            if not cur:
                # cur now becomes the first node of the next level
                cur = nxt
                # nxt becomes the first node's left child in that new level
                nxt = cur.left

        # Return the root of the tree (now with next pointers set)
        return node

lst = [1,2,3,4,5,6,7]

root = list_to_binary_tree(lst)
res = Solution().connect(root)

print_tree(root)
