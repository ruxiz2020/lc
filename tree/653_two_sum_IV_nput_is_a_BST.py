class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()
        s = [root]
        while s:
            cur = s.pop()
            if k - cur.val in nums:
                return True
            nums.add(cur.val)
            if cur.left:
                s.append(cur.left)
            if cur.right:
                s.append(cur.right)
        return False
