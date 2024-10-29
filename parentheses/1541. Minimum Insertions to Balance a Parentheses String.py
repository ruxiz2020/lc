class Solution:
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
