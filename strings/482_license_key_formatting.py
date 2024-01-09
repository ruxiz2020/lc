class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        ss = s.replace("-", "").upper()
        sub_len = len(ss) // k
        first_len = len(ss) % k

        first_ss = []
        if first_len > 0:
            first_ss.append(ss[:first_len])

        rest_ss = [ss[first_len:][i:i+k] for i in range(0, len(ss[first_len:]), k)]

        return "-".join(first_ss + rest_ss)

