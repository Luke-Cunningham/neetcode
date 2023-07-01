
class TwoPointers:

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        chars = []
        for i in s:
            if i.isalnum():
                chars.append(i)
        return chars == chars[::-1]
