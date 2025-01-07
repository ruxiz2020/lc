

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    O(N)
    O(N)
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]



# Test Linked List:
# Node 1 -> Node 2 -> Node 3
# Random pointers:
# Node 1.random -> Node 3
# Node 2.random -> Node 1
# Node 3.random -> Node 2

def create_linked_list():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.next = node2
    node2.next = node3

    node1.random = node3
    node2.random = node1
    node3.random = node2

    return node1

# Function to print the linked list for testing
def print_list(head):
    cur = head
    while cur:
        print(f"Node({cur.val}), Random({cur.random.val if cur.random else 'None'})")
        cur = cur.next

# Test the Solution
original_list = create_linked_list()
solution = Solution()
cloned_list = solution.copyRandomList(original_list)

print("Original list:")
print_list(original_list)

print("\nCloned list:")
print_list(cloned_list)
