class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
tc : O(n)
我们每次贪心的找在自己当前能到达的几个位置里面，跳到哪个位置的时候，在下一步能跳的最远。然后，我们当前步就跳到这个位置上去，所以我们在这一步的跳跃时，给下一步留下了最好的结果。

所以，使用一个cur表示当前步能到达的最远位置，使用pre表示上一次能到达的最远位置。所以，我们应该遍历在上一步的覆盖范围内，当前能跳的最远位置来更新cur。一个节省计算资源的方式是，保存以前已经检查了的位置为Pos，这样每次检查的范围是pos~pre。
————————————————
版权声明：本文为CSDN博主「负雪明烛」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/84578893
        """
        reach = 0
        cur = 0
        N = len(nums)
        count = 0
        pos = 0
        while cur < N - 1:
            count += 1
            pre = cur
            while pos <= pre:
                cur = max(cur, pos + nums[pos])
                pos += 1
        return count
