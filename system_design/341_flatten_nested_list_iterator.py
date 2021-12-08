import collections

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = collections.deque()
        def getAll(nests):
            for nest in nests:
                if type(nest)==int:
                    self.queue.append(nest)
                else:
                    getAll(nest)
        getAll(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.queue.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue)



if __name__ == '__main__':

    nestedList = [[1,1],2,[1,1]]
    nestedList = [1,[4,[6]]]

    ss = NestedIterator(nestedList)

    print(ss.queue)

    i = NestedIterator(nestedList)
    while i.hasNext():
        print(i.next())
