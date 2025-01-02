class Solution:
    """
    This code determines whether a string s can be transformed into a 
    palindrome by removing at most k characters, using the 
    Longest Palindromic Subsequence (LPS) to calculate the minimum number of characters 
    that need to be removed.

    The _longestPalindromeSubseq function employs a dynamic programming approach, 
    where dp[i][j] stores the LPS length for the substring s[i..j], 
    building up results from smaller substrings to the full string by 
    considering character matches and mismatches.

    The main function compares the required removals (len(s) - LPS_length) 
    to k and returns True if they are within the allowable limit, 
    with a time complexity of 
    Time Complexity: O(n^2) due to the dynamic programming LPS computation.
    Space Complexity: O(n^2) for the dp table.
    """

    def isValidPalindrome(self, s: str, k: int) -> bool:
        """
        Check if string s can become a palindrome by removing at most k characters.
        """
        # Calculate how many removals are needed to achieve the LPS.
        # If the needed removals <= k, then it's possible to form a palindrome.
        return len(s) - self._longestPalindromeSubseq(s) <= k

    def _longestPalindromeSubseq(self, s: str) -> int:
        """
        Returns the length of the Longest Palindromic Subsequence (LPS) in s.
        Uses a bottom-up dynamic programming approach.

        dp[i][j] will store the length of the LPS of the substring s[i..j].
        """
        n = len(s)
        # Initialize a 2D dp array with all zeros: dp[i][j] = 0 by default.
        dp = [[0] * n for _ in range(n)]

        # Every single character is a palindrome of length 1.
        for i in range(n):
            dp[i][i] = 1

        # d is the 'distance' between i and j. We expand substrings by length.
        # For d = 1 to n-1, we fill dp[i][i+d].
        for d in range(1, n):
            # i goes from 0 up to (n - d - 1), ensuring j = i + d is within bounds.
            for i in range(n - d):
                j = i + d  # j is the ending index of the substring

                print(i, j)  # Debug: show which substring indices we are considering

                if s[i] == s[j]:
                    # If the characters match, the LPS length is
                    # 2 plus the LPS of the substring inside (i+1, j-1).
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                    print("same", (i + 1, j - 1), (i, j))  # Debug info
                    for row in dp:
                        print(row)  # Debug: print current state of dp
                else:
                    # If they don't match, the LPS is the maximum of:
                    #   - LPS of the substring (i+1, j)
                    #   - LPS of the substring (i, j-1)
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    print("diff")  # Debug info
                    for row in dp:
                        print(row)  # Debug: print current state of dp

        print(dp[0][n - 1])  # Debug: final result of LPS for s[0..n-1]
        return dp[0][n - 1]


"""
[1, 1, 1, 1, 1, 3, 5]
[0, 1, 1, 1, 1, 3, 3]
[0, 0, 1, 1, 1, 3, 3]
[0, 0, 0, 1, 1, 1, 1]
[0, 0, 0, 0, 1, 1, 1]
[0, 0, 0, 0, 0, 1, 1]
[0, 0, 0, 0, 0, 0, 1]
"""
s = "abcdeca"; k = 2

#s = "abbababa"; k = 1

"""
0 (1) 2 3 4 5
1 1 (2)    (last)
2   1 (3)
3     1
4       1
5         1
"""

ss = Solution()
res = ss.isValidPalindrome(s, k)
print(res)
