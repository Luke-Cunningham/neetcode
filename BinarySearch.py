class BinarySearch:

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return -1

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        r, c = len(matrix), len(matrix[0])
        start, end = 0, r * c - 1

        while start <= end:
            mid = (start + end) // 2
            num = matrix[mid / c][mid % c]

            if num == target:
                return True
            elif num < target:
                start = mid + 1
            else:
                end = mid - 1

        return False
