class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        pre = chars[0]
        count = 0
        pos = 0
        for ch in chars:
            if pre == ch:
                count += 1
            else:
                chars[pos] = pre
                pos += 1
                if count > 1:
                    count = str(count)
                    for i in range(len(count)):
                        chars[pos] = count[i]
                        pos += 1
                count = 1
                pre = ch
        chars[pos] = pre
        pos += 1
        if count > 1:
            count = str(count)
            for i in range(len(count)):
                chars[pos] = count[i]
                pos += 1
        return pos
