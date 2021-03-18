class FileSystem(object):

    def __init__(self):
        self.data = {"": -1}


    def createPath(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        if path[:path.rfind("/")] not in self.data \
           or path in self.data:
            return False
        self.data[path] = value
        return True

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        return self.data.get(path, -1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
