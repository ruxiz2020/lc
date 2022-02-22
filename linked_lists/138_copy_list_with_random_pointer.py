class Solution:
    def __init__(self):
        self.visit = {None: None}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head in self.visit:
            return self.visit[head]
        node = Node(head.val, None, None)
        self.visit[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
