class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2147483647; INT_MIN = -2147483648
        sum = 0
        sign = 1
        i = 0
        if s == '':
            return 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] == '-':
            sign = -1
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            i += 1
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if INT_MAX/10 >= sum:
                sum *= 10
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            if INT_MAX - digit >= sum:
                sum += digit
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            i += 1
        return sign*sum
