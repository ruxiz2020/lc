class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        # base case
        if len(s) != len(goal):
            return False
        # same str and check dup
        seen = set()
        if s == goal:
            for a in s:
                if a in seen:
                    return True
                else:
                    seen.add(a)
            return False

        pair = None
        res = 0
        # check if pair exist
        for i in range(len(s)):
            if s[i] != goal[i]:
                if not pair:
                    pair = (s[i], goal[i])
                    print(pair)
                elif pair == (goal[i], s[i]):
                    res += 1
                else:
                    return False

        if pair is None or res==1:
            return True

        return False

if __name__ == '__main__':

    s = "ab"
    goal = "ba"

    s = "aa"
    goal = "aa"

    s = "acdd"
    goal = "adcc"
    ss = Solution()
    res = ss.buddyStrings(s, goal)

    print(res)
