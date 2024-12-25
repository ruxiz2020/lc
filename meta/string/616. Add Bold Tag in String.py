class Solution:
    """
    O(n * k * l) k: number of words, l: avg length of words
    O(n)
    """
    def addBoldTag(self, s: str, words: list[str]) -> str:
        # Length of the input string
        n = len(s)

        # This list will hold parts of the final output string.
        ans = []

        # 'bold' array indicates whether a character in s should be bolded.
        # bold[i] = 1 (True) if s[i] should be bolded, otherwise 0 (False).
        bold = [0] * n

        # 'boldEnd' keeps track of the furthest index we know should be bolded
        # based on the words we've matched so far.
        boldEnd = -1

        # Iterate over each character in s.
        for i in range(n):
            # For each position i, check if any word in 'words' starts at s[i:].
            for word in words:
                # If s[i:] begins with 'word', update boldEnd.
                # This means s[i : i+len(word)] needs to be bolded.
                if s[i:].startswith(word):
                    boldEnd = max(boldEnd, i + len(word))

            # After checking all words, if boldEnd > i, it means the character at index i
            # is within a bolded substring.
            bold[i] = 1 if boldEnd > i else 0

        # Now we have a 'bold' array indicating which chars need bolding.

        # Construct the final string with '<b></b>' tags.
        i = 0
        while i < n:
            if bold[i]:
                # If the current character should be bolded,
                # find the continuous range of bolded characters starting at i.
                j = i
                while j < n and bold[j]:
                    j += 1
                # Now s[i:j] is a continuous bolded substring.
                ans.append('<b>' + s[i:j] + '</b>')
                i = j  # Move past the bolded block.
            else:
                # If the current character should not be bolded, just append it.
                ans.append(s[i])
                i += 1

        # Join all parts and return the resultant string.
        return ''.join(ans)



s = "abcxyz123"; words = ["abc","123"]

res = Solution().addBoldTag(s, words)
print(res) #<b>abc</b>xyz<b>123</b>
