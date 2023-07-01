from ArraysAndHashing import ArraysAndHashing
from BinarySearch import BinarySearch
from TwoPointers import TwoPointers

if __name__ == '__main__':
    p1 = ArraysAndHashing()

    case1 = [1, 2, 3, 1]
    p1.containsDuplicate(case1)

    s, t = "nagaram", "anagram"
    p1.isAnagram(s, t)

    case1, t1 = [2, 7, 11, 15], 9
    case2, t2 = [3,3], 6
    p1.twoSum(case1, t1)

    ####################################################################################################################

    p2 = TwoPointers()

    case1 = "A man, a plan, a canal: Panama"

    ####################################################################################################################

    p5 = BinarySearch()