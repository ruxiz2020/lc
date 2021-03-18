# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        (BFS Straight Forward Answer)
        """
        if root is None:
            return []
        queue = collections.deque([root])
        res = []
        flag = True #left->right
        while queue:
            tmp = []
            for _ in range(len(queue)):
                if flag:
                    node = queue.popleft()
                    tmp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.pop()
                    tmp.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
            flag = not flag
            res.append(tmp)
        return res
