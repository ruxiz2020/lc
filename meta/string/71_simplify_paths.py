class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
模拟整个过程：

1. "/" 根目录
2. ".." 跳转上级目录，上级目录为空，所以依旧处于 "/"
3. "a" 进入子目录a，目前处于 "/a"
4. "b" 进入子目录b，目前处于 "/a/b"
5. "c" 进入子目录c，目前处于 "/a/b/c"
6. "." 当前目录，不操作，仍处于 "/a/b/c"
7. ".." 返回上级目录，最终为 "/a/b"
使用一个栈来解决问题。遇到'..'弹栈，遇到'.'不操作，其他情况下压栈。
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
