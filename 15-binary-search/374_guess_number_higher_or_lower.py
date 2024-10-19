# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2  # Calculate mid to avoid overflow
            result = guess(mid)  # Call guess API
            if result == 0:
                return mid  # Correct guess
            elif result == -1:
                right = mid - 1  # Target is lower
            else:
                left = mid + 1  # Target is higher


# Time: O(log n)
# Space: O(1)
