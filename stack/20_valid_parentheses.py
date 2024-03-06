class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        O(n)
        """
        if len(s) == 0: return True
        d = {')':'(', '}': '{', ']':'['}
        stack = []
        for char in s:
            if char not in d:
                stack.append(char)
            else:
                if len(stack) == 0 or d[char] != stack.pop():
                    return False

        return len(stack) == 0


if __name__ == '__main__':

    s = "()[]{}"

    ss = Solution()
    res = ss.isValid(s)

    print(res)
