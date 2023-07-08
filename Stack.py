
class Stack:

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map.keys():
                if not stack or bracket_map[char] != stack.pop():
                    return False
        return not stack


class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """

        if not self.stack:
            self.stack.append((val, val))
        else:
            curr_min = self.stack[-1][1]
            new_min = min(val, curr_min)
            self.stack.append((val, new_min))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.rowCheck(board) and self.colCheck(board) and self.subSquareCheck(board)


    def rowCheck(self, board):
        for row in board:
            if not self.listCheck(row):
                return False
        return True

    def colCheck(self, board):
        for col in zip(*board):
            if not self.listCheck(col):
                return False
        return True

    def subSquareCheck(self, board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subSquare = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.listCheck(subSquare):
                    return False
        return True

    def listCheck(self, listToCheck):
        listToCheck = [i for i in listToCheck if i != '.']
        return len(listToCheck) == len(set(listToCheck))