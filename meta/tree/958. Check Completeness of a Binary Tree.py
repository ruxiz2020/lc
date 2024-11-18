# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def list_to_binary_tree(lst):
    if not lst or lst[0] is None:
        return None

    # Create the root of the tree
    root = TreeNode(lst[0])
    queue = [root]  # Queue to keep track of nodes to attach children to
    index = 1  # Start from the second element in the list

    while index < len(lst):
        node = queue.pop(0)

        # Add left child
        if index < len(lst) and lst[index] is not None:
            node.left = TreeNode(lst[index])
            queue.append(node.left)

        index += 1  # Move to the next element

        # Add right child
        if index < len(lst) and lst[index] is not None:
            node.right = TreeNode(lst[index])
            queue.append(node.right)

        index += 1  # Move to the next element

    return root

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = []
        if root is None:
            return True
        queue.append(root)
        flag = False
        while queue:
            node = queue.pop(0)
            if flag is False:
                if node.left and node.right:
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    flag = True # not complete row found
                    if node.left:
                        queue.append(node.left)
                    elif node.right:
                        return False # found right but no left
            elif flag is True: #the last level was incomplete, and there is more row
                if node.left or node.right:
                    return False
        return True


lst = [1,2,3,4,5,6]
lst = [1,2,3,4,5,None,7]
root = list_to_binary_tree(lst)
res = Solution().isCompleteTree(root)
print(res) #True
