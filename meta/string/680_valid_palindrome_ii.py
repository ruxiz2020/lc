class Solution:
    """
    This code checks if a given string s can become a palindrome by removing 
    at most one character, using two pointers (l and r) to compare characters 
    from both ends.

    If a mismatch is found between s[l] and s[r], it verifies whether skipping 
    either the character at l or at r forms a valid palindrome by slicing the 
    string and comparing it to its reverse.

    The algorithm runs in 
    O(N) time and uses 
    O(N) space for the string slicing operations during palindrome checks.
    O(N)
    O(N)
    """
    def validPalindrone(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skip_l, skip_r = s[l + 1: r + 1], s[l: r]
                return (skip_l == skip_l[::-1]
                        or skip_r == skip_r[::-1])
            l, r = l + 1, r - 1
        return True


s = "abca"
res = Solution().validPalindrone(s)
print(res) # True
