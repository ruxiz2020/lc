

class Solution:
  def connect(self, node: 'Optional[Node]') -> 'Optional[Node]':

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
