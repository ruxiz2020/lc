from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dict_char = Counter(chars)

        dicts = []
        for w in words:
            dicts.append(Counter(w))

        res = 0
        for d in dicts:
            next_word = False
            for k in d.keys():
                if k not in dict_char:
                    next_word = True
                    #print(d)
                    break
                if k in dict_char and d[k] > dict_char[k]:
                    next_word = True
                    #print(d)
                    break
            if next_word: continue
            print(d)
            res += sum(d.values())
        return res

if __name__ == '__main__':

    words = ["cat","bt","hat","tree"]; chars = "atach"

    words = ["hello","world","leetcode"]; chars = "welldonehoneyr"
    ss = Solution()
    res = ss.countCharacters(words, chars)
    print(res)
