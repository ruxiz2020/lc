class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''O(n), O(n)'''
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
