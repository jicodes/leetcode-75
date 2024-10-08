from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        size = len(flowerbed)
        for i in range(size):
            if flowerbed[i] == 0:
                is_left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                is_right_empty = (i == size - 1) or (flowerbed[i + 1] == 0)

                if is_left_empty and is_right_empty:
                    flowerbed[i] = 1
                    count += 1

                    if count >= n:
                        return True

        return count >= n
