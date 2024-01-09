class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        while i < len(name):
            if j >= len(typed):
                return False
            if name[i] != typed[j]:
                if j == 0 or typed[j-1] != typed[j]:
                    return False
                j += 1
            else:
                i += 1
                j += 1

        while j < len(typed):
            if typed[j-1] != typed[j]:
                return False
            j += 1
        return j == len(typed)


if __name__ == '__main__':

    name = "alex"
    typed = "aaleex"

    name = "vtkgn"
    typed = "vttkgnn"

    ss = Solution()
    res = ss.isLongPressedName(name, typed)

    print(res)


