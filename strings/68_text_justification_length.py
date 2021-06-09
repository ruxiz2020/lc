class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]

        Input: words = ["This", "is", "an", "example",
        "of", "text", "justification."], maxWidth = 16
        Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
        """
        ans = []
        i = 0
        while i < len(words):
            size = 0
            begin = i
            while i < len(words):
                if size == 0:
                    newsize = len(words[i])
                else:
                    newsize = size + len(words[i]) + 1
                if newsize <= maxWidth:
                    size = newsize
                else:
                    break
                i += 1
            spaceCnt = maxWidth - size
            if i - begin - 1 > 0 and i < len(words):
                everyCount = spaceCnt // (i - begin - 1)
                spaceCnt %= i - begin - 1
            else:
                everyCount = 0
            j = begin;s=""
            while j < i:
                if j == begin:
                    s = words[j]
                else:
                    s += ' ' * (everyCount + 1)
                    if spaceCnt > 0 and i < len(words):
                        s += ' '
                        spaceCnt -= 1
                    s += words[j]
                j += 1
            s += ' ' * spaceCnt
            ans.append(s)
        return ans
