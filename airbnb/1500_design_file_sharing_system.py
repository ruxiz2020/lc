class FileSharing(object):

    def __init__(self, m):
        """
        :type m: int
        """
        self.users = defaultdict(set) # e.g. user1: { file1, file2... }
        self.files = defaultdict(set) # e.g. file1: { user1, user2... }
        self.lefts = [] # minheap

    def join(self, ownedChunks):
        """
        :type ownedChunks: List[int]
        :rtype: int
        """
        userId = len(self.users) + 1
        if len(self.lefts) > 0:
            userId = heappop(self.lefts)
        self.users[userId] = set(ownedChunks)
        for c in ownedChunks:
            self.files[c].add(userId)
        return userId



    def leave(self, userID):
        """
        :type userID: int
        :rtype: None
        """
        if userID not in self.users:
            return
        for c in self.users[userID]:
            self.files[c].remove(userID)
        self.users[userID] = set()
        heappush(self.lefts, userID)


    def request(self, userID, chunkID):
        """
        :type userID: int
        :type chunkID: int
        :rtype: List[int]
        """
        arr = list(self.files[chunkID])
        arr.sort()
        if len(arr) > 0:
            self.users[userID].add(chunkID)
            self.files[chunkID].add(userID)
        return arr



# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)
