from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict = {c: i for i, c in enumerate(order)}
        words = [[dict[c] for c in word] for word in words]
        print(words)
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if dict[w2[j]] < dict[w1[j]]:
                        return False
                    break
        return True


if __name__ == '__main__':

    words = ["word","world","row"]
    order = "worldabcefghijkmnpqstuvxyz"

    ss = Solution()
    res = ss.isAlienSorted(words, order)
    print(res)
