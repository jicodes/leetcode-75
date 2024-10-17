from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Step 1: Count the occurrences of each number
        count_map = {}
        for num in arr:
            count_map[num] = count_map.get(num, 0) + 1

        # Step 2: Check if the occurrences are unique
        freq_set = set(count_map.values())

        # Step 3: Compare the size of the frequency set and the count map
        return len(freq_set) == len(count_map)
