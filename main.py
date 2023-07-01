from ArraysAndHashing import ArraysAndHashing
from BinarySearch import BinarySearch
from TwoPointers import TwoPointers
from SlidingWindow import SlidingWindow
from Stack import Stack

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
    p2.isPalindrome(case1)

    ####################################################################################################################

    p3 = SlidingWindow()
    case1 = [7, 1, 5, 3, 6, 4]
    p3.maxProfit(case1)

    ####################################################################################################################

    p4 = Stack()

    ####################################################################################################################
    p5 = BinarySearch()