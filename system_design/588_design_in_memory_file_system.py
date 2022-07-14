class FileSystem(object):

    def __init__(self):
        self.root = {'dirs' : {}, 'files': {}}


    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        node, type = self.getExistedNode(path)
        if type == 'dir': return sorted(list(node['dirs'].keys()) + \
                            list(node['files'].keys()))
        return [path.split('/')[-1]]

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        node = self.root
        for dir in filter(lambda x: len(x)>0, path.split('/')):
            if dir not in node['dirs']: node['dirs'][dir] = {'dirs' : {}, 'files': {}}
            node = node['dirs'][dir]

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        dirs = filePath.split('/')
        path, file = '/'.join(dirs[:-1]), dirs[-1]
        self.mkdir(path)
        node, type = self.getExistedNode(path)
        if file not in node['files']: node['files'][file] = ''
        node['files'][file] += content


    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        dirs = filePath.split('/')
        path, file = '/'.join(dirs[:-1]), dirs[-1]
        node, type = self.getExistedNode(path)
        return node['files'][file]

    def getExistedNode(self, path):
        """
        :type path: str
        :rtype: str
        """
        node = self.root
        for dir in filter(len, path.split('/')):
            if dir in node['dirs']: node = node['dirs'][dir]
            else: return node, 'file'
        return node, 'dir'


fileSystem = FileSystem();
fileSystem.ls("/");                         # return []

print(fileSystem.root)

fileSystem.mkdir("/a/b/c");

print(fileSystem.root)


fileSystem.addContentToFile("/a/b/c/d", "hello");

print(fileSystem.root)

fileSystem.ls("/");                         # return ["a"]

print(fileSystem.root)

fileSystem.readContentFromFile("/a/b/c/d"); # return "hello"

print(fileSystem.root)
