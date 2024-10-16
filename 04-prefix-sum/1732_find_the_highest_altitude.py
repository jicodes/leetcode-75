from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_altitude = 0  # Starting altitude
        max_altitude = 0  # Max altitude so far

        # Iterate through gain array
        for g in gain:
            curr_altitude += g  # Update current altitude
            max_altitude = max(
                max_altitude, curr_altitude
            )  # Update max altitude if needed

        return max_altitude
