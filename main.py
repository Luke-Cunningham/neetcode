from ArraysAndHashing import ArraysAndHashing
from BinarySearch import BinarySearch

if __name__ == '__main__':
    p1 = ArraysAndHashing()
    p5 = BinarySearch()

    case1 = [1, 2, 3, 1]
    p1.containsDuplicate(case1)

    s, t = "nagaram", "anagram"
    p1.isAnagram(s, t)

    case1, t1 = [2, 7, 11, 15], 9
    case2, t2 = [3,3], 6
    p1.twoSum(case1, t1)