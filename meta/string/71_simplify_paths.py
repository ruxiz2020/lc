class Solution(object):
    def simplifyPath(self, path):
        """
        This code simplifies an absolute Unix-style file path by splitting the path 
        into components separated by /, then using a stack to process valid directory 
        names, ignoring . and handling .. by popping the last directory from the stack 
        if possible.

        The traversal iterates through the string to identify path components, 
        appending valid directory names to the stack and ignoring empty components or 
        unnecessary current directory markers (.).

        After processing, the stack contains the simplified path components, 
        which are joined with / to form the final simplified path, ensuring 
        the output adheres to Unix path conventions.

        O(N)
        O(N)
        """
        stack = []
        i = 0
        res = ''
        while i < len(path):
            end = i + 1 # to skip /
            while end < len(path) and path[end] != "/":
                end += 1
            sub = path[i + 1:end]
            print(sub)
            if len(sub) > 0:
                if sub == "..":
                    if stack != []: stack.pop()
                elif sub != ".":
                    stack.append(sub)
            i = end
        if stack == []: return "/"
        for i in stack:
            res += "/" + i
        return res


path = "/home//foo/"
path = "/home/./foo/"
res = Solution().simplifyPath(path)
print(res) # /home/foo
