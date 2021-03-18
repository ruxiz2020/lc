# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
This question can be solved by Breadth First Search.

The answer is very direct, use bfs to traversal level by level and for each level we loop through node and append them all to a tmp list, then we append the tmp list to the answer list and return. To apply FIFO, we can use deque for popleft()
        """
        if root is None: return []
        queue, res = collections.deque([root]),[]
        while queue:
            size = len(queue)
            tmp=[]
            while size>0:
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size-=1
            res.append(tmp)
        return res
