class Solution:
    def wordPatternMatch(self, pattern, str):
        def match(i, j):
            is_match = False
            if i == len(pattern) and j == len(str):
                is_match = True

            elif i < len(pattern) and j < len(str):
                p = pattern[i]
                if p in p2w:
                    w = p2w[p]
                    if w == str[j:j + len(w)]:
                        is_match = match(i + 1, j + len(w))
                else:
                    for k in range(j, len(str)):
                        w = str[j:k + 1]
                        if w not in w2p:
                            w2p[w], p2w[p] = p, w
                            is_match = match(i + 1, k + 1)
                            w2p.pop(w)
                            p2w.pop(p)

                        if is_match:
                            break
            return is_match

        w2p = {}
        p2w = {}
        return match(0, 0)


if __name__ == '__main__':

    pattern = "abab"； s = "redblueredblue"

    ss = Solution()
    res = ss.wordPattern(pattern, s)
    print(res)
