class Solution:
    """
    This code identifies substrings of the input string s that match any word 
    in the list words and wraps these substrings in <b></b> tags, 
    using a bold array to track which characters should be bolded.

    It iterates over the string, marking ranges of bolded characters whenever 
    a word from words matches a substring starting at the current position, 
    and then constructs the output string by appending bolded or non-bolded segments 
    accordingly.

    The algorithm handles overlapping and continuous bolded ranges efficiently 
    by extending the range (boldEnd) and ensures minimal <b></b> tags in the output, 
    with time complexity 
    O(n⋅k⋅l), where 
    k is the number of words, 
    l is the average word length, and 
    n is the length of the string.

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
        print(bold) # [1, 1, 1, 0, 0, 0, 1, 1, 1]

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
