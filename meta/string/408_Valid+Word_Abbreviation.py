class Solution:
    """
    O(M + N)
    O(1)
    """
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m, n = len(word), len(abbr)
        i = j = num = 0
        while i < m and j < n:
            if abbr[j].isdigit():
                if abbr[j] == "0" and num == 0:
                    return False
                num = num * 10 + int(abbr[j])
            else:
                i += num
                num = 0
                if i >= m or word[i] != abbr[j]:
                    return False
                i += 1
            j += 1
            print(i, num)
        return i + num == m and j == n


ss = Solution()

word = "listofitemsisgoods"
abbr = "l1s15"

res = ss.validWordAbbreviation(word, abbr)
print(res) # True
