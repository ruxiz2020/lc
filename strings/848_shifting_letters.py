class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        _len = len(S)
        shifts_sum = sum(shifts)
        shifts_real = []
        for shift in shifts:
            shifts_real.append(shifts_sum)
            shifts_sum -= shift

        print(shifts_real)
        def shift_map(string, shift_time):
            shifted = ord(s) + (shift_time % 26)
            return chr(shifted if shifted <= ord('z') else shifted - 26)
        ans = ''
        for i, s in enumerate(S):
            ans += shift_map(s, shifts_real[i])
        return ans

if __name__ == '__main__':

    s = "abc"; shifts = [3,5,9]

    ss = Solution()
    res = ss.shiftingLetters(s, shifts)
    print(res)
