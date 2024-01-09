class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return not re.match(".*A.*A.*", s) and not re.match(".*LLL.*", s)


class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        N = len(s)
        s = s + "P"
        countA = 0
        countL = 0
        for i in range(N):
            if s[i] == "A":
                countA += 1
            if countA > 1:
                return False
            if s[i] == "L":
                countL += 1
                if countL >= 3:
                    return False
            else:
                countL = 0
        return True


class Solution:
    def checkRecord(self, s: str) -> bool:
        # Check for less than two Absents
        less_than_two_absents = s.count('A') < 2

        # Check for not having three continuous Lates
        no_three_continuous_lates = 'LLL' not in s

        # Return True if both conditions are met, otherwise False
        return less_than_two_absents and no_three_continuous_lates
