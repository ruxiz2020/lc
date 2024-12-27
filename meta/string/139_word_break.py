class Solution:
    def wordBreak(self, s, wordDict):
        """
        Check if string s can be segmented into words present in wordDict.

        Time Complexity: O(N^2 * M)
          - N is the length of s.
          - We have a nested loop i from 1..N and j from 0..i, so ~O(N^2).
          - Checking if s[j:i] is in wordDict can be O(M) in the worst case
            (depending on the data structure used for wordDict).
            - If wordDict is a hash set, then lookup is O(len(s[j:i])) = O(N) worst,
              or considered O(1) average if we assume hashing is constant-time.
            - The provided notation suggests we consider average word length M.

        Space Complexity: O(N)
          - We use a dp array of size N+1.
        """

        L = len(s)
        # dp[i] means: "Can we break s[:i] into valid words from wordDict?"
        dp = [False] * (L + 1)
        # Base case: an empty string can always be segmented trivially
        dp[0] = True

        # For each endpoint i from 1 to L (inclusive),
        # we check all possible split points j, where 0 <= j < i.
        for i in range(1, L + 1):
            for j in range(i):
                # If s[:j] can be broken and s[j:i] is a word in the dictionary,
                # then s[:i] can be broken as well.
                if dp[j] and s[j:i] in wordDict:
                    print(s[j:i])  # Debug print to see which substrings match
                    dp[i] = True
                    # Once dp[i] is True, we can stop checking further splits
                    # for this i, since we already know s[:i] is breakable.
                    break

        print(dp)  # Debug print to see the dp array state
        return dp[-1]  # Return whether the entire string s[:L] is breakable



if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]

    ss = Solution()
    res = ss.wordBreak(s, wordDict)
    print(res)
