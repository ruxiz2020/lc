
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next



class Solution:
    """
    This code inserts a new node with a given value insertVal into a sorted circular 
    linked list, maintaining the sorted order by traversing the list and finding 
    the appropriate position based on the node values.

    It handles edge cases where the list is empty by creating a single-node circular 
    list and checks whether the new value fits between the current node (prev) 
    and the next node (curr), or if it needs to be inserted at the end of the list 
    where the order wraps around.
    O(n)
    O(1)
    """
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if head is None:
            node.next = node
            return node
        prev, curr = head, head.next
        while curr != head:
            if prev.val <= insertVal <= curr.val or (
                prev.val > curr.val and \
                (insertVal >= prev.val or insertVal <= curr.val)
            ):
                break
            prev, curr = curr, curr.next
        prev.next = node
        node.next = curr
        return head


# Test Circular Linked List:
# Initial List: 1 -> 3 -> 4 -> 1 (circular)
# Insert Value: 2

def create_circular_linked_list():
    node1 = Node(1)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node3
    node3.next = node4
    node4.next = node1

    return node1

# Function to print the circular linked list for testing
def print_circular_list(head, count):
    cur = head
    result = []
    while count > 0:
        result.append(cur.val)
        cur = cur.next
        count -= 1
    print(" -> ".join(map(str, result)))

# Test the Solution
circular_list = create_circular_linked_list()
solution = Solution()

print("Original circular list:")
print_circular_list(circular_list, 6)  # Print the first 6 nodes for clarity

# Insert a new value into the circular linked list
inserted_list = solution.insert(circular_list, 2)

print("\nCircular list after insertion:")
print_circular_list(inserted_list, 7)  # Print the first 7 nodes to include the new insertion
