import collections


class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        keyToStrings = collections.defaultdict(list)

        def getKey(s: str) -> str:
            """
            Returns the key of 's' by pairwise calculation of differences.
            e.g. getKey("abc") -> "1,1" because diff(a, b) = 1 and diff(b, c) = 1.
            """
            diffs = []

            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i - 1]) + 26) % 26
                print(diff)
                diffs.append(str(diff))

            return ','.join(diffs)

        for s in strings:
            print(getKey(s))
            keyToStrings[getKey(s)].append(s)

        print(keyToStrings)
        return keyToStrings.values()


strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

ss = Solution()
ss.groupStrings(strings)
