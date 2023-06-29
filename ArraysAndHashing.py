
class ArraysAndHashing:

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique = set(nums)

        return len(unique) != len(nums)

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        for c in set(s):
            if s.count(c) != t.count(c):
                return False

        return True

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i,x in enumerate(nums):
            for j,y in enumerate(nums):
                if x + y == target and i != j:
                    return i,j