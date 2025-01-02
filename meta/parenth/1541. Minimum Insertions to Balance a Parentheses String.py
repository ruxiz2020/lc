class Solution:
    """
    This code calculates the minimum number of insertions needed to balance a string 
    of parentheses, where every ( must be matched with exactly two ) in the correct order. 
    It iterates through the string, maintaining a balance to track unmatched opening 
    parentheses and incrementing insertions_needed for unmatched or extra closing 
    parentheses.

    During the traversal, it handles consecutive ) pairs efficiently and ensures 
    that unmatched ( are accounted for by requiring two additional ) for each unmatched 
    opening parenthesis.

    At the end, any leftover unmatched ( are balanced with 2 insertions each, 
    and the final result is returned as the total number of insertions needed 
    to make the string valid.
    """
    def min_insertions(self, s: str) -> int:
        # 'balance' keeps track of the balance of the parentheses
        # 'insertions_needed' will be the answer, representing the minimum insertions needed
        insertions_needed = balance = 0
        i, n = 0, len(s)  # 'i' is the current position, 'n' is the length of the string

        while i < n:  # Iterate through the string
            if s[i] == '(':  # If the current character is an opening parenthesis
                balance += 1  # Increase balance
            else:  # If the current character is a closing parenthesis
                # Check if there's a consecutive closing parenthesis
                if i < n - 1 and s[i + 1] == ')':
                    i += 1  # Move to the next character as we've found a pair "))"
                else:
                    # If a pair wasn't found, one insertion is needed
                    insertions_needed += 1
                # If there is no unmatched opening parenthesis
                if balance == 0:
                    # We need an insertion for an opening parenthesis
                    insertions_needed += 1
                else:
                    # Otherwise, use one unmatched opening to balance a pair "))"
                    balance -= 1
            i += 1  # Move to the next character

        # After processing the entire string, we might have unmatched opening parentheses
        # Each of these needs two insertions to be balanced (one opening parenthesis needs "))")
        insertions_needed += balance * 2

        return insertions_needed  # Return the total number of insertions needed


s = "(()))"
res = Solution().min_insertions(s)
print(res)
