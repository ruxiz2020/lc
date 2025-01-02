# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    This code parses a string representation of a binary tree to construct the tree, 
    using a recursive depth-first search (DFS) approach where the substring 
    before the first ( is the root node, and subsequent segments in parentheses 
    represent left and right subtrees.

    The function tracks parentheses using a counter to identify complete segments 
    for each child subtree, then recursively parses these segments to construct 
    the left and right child nodes of the current root.

    After processing the entire string, the function returns the root of the 
    constructed tree.
    O(N): The function processes each character of the input string at most once.
    O(H): The space complexity is related to the height of the tree formed, due to recursion.
    """
    def str2tree(self, s: str) -> TreeNode:

        # Define a recursive function that builds the tree from a substring.
        def dfs(s):
            # If the substring is empty, return None (no node to form).
            if not s:
                return None

            p = s.find('(')
            if p == -1:
                return TreeNode(int(s))

            # Create the root node using the substring before the first '(' as its value.
            root = TreeNode(int(s[:p]))

            # 'start' keeps track of where we started parsing children.
            start = p

            cnt = 0
            # Iterate through the substring from the first '(' to the end.
            for i in range(p, len(s)):
                if s[i] == '(':
                    cnt += 1
                elif s[i] == ')':
                    cnt -= 1

                # When 'cnt' returns to 0, we've found a complete segment representing a child subtree.
                if cnt == 0:
                    # If this is the first child (the left child),
                    # 'start == p' indicates we haven't parsed the left child yet.
                    if start == p:
                        # Debug prints to show the substring for the left child.
                        print("left" + s[start + 1 : i])
                        # Recursively parse the substring inside these parentheses for the left child.
                        root.left = dfs(s[start + 1 : i])

                        # Update 'start' to indicate we finished parsing the left child subtree.
                        start = i + 1
                    else:
                        # Debug prints to show the substring for the right child.
                        print("right" + s[start + 1 : i])
                        # Recursively parse the substring for the right child.
                        root.right = dfs(s[start + 1 : i])

            # Return the constructed root node (with its left and/or right children).
            return root

        # Initiate the recursive parsing of the entire string.
        return dfs(s)



s = "4(2(3)(1))(6(5))"

res = Solution().str2tree(s)
