# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list as None

    def append(self, data):
        # Create a new node
        new_node = ListNode(data)
        if not self.head:  # If the linked list is empty
            self.head = new_node
            return
        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        # Add the new node at the end
        current.next = new_node

    def display(self):
        # Display the linked list elements
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# Convert a Python list to a linked list
def list_to_linked_list(lst):
    linked_list = LinkedList()
    for item in lst:
        linked_list.append(item)
    return linked_list

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        beforeHead = ListNode(0)
        afterHead = ListNode(0)
        before = beforeHead
        after = afterHead

        while head:
            if head.val < x:
                before.next = head
                before = head
            else:
                after.next = head
                after = head
            head = head.next

        after.next = None
        before.next = afterHead.next

        return beforeHead.next


lst = [1,4,3,2,5,2]; x = 3 # res [1,2,2,4,3,5]
head = list_to_linked_list(lst)

res = Solution().partition(head, x)

current = res
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
