class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.maxCnt = 0
        self.stack = {}

    def push(self, val: int) -> None:
        valCnt = 1 + self.cnt.get(val, 0)
        self.cnt[val] = valCnt
        if valCnt > self.maxCnt:
            self.maxCnt = valCnt
            self.stack[valCnt] = []
        self.stack[valCnt].append(val)

    def pop(self) -> int:
        res = self.stack[self.maxCnt].pop()
        self.cnt[res] -= 1
        if not self.stack[self.maxCnt]:
            self.maxCnt -= 1
        return res

