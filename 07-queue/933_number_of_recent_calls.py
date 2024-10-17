from collections import deque


class RecentCounter:
    def __init__(self):
        self.calls = deque()  # Queue to hold the timestamps of calls

    def ping(self, t: int) -> int:
        self.calls.append(t)  # Add the new call timestamp

        # Remove calls that are older than 3000 ms
        while self.calls and self.calls[0] < t - 3000:
            self.calls.popleft()  # Remove the old timestamps

        return len(self.calls)  # Return the count of recent calls


# Example usage:
# recentCounter = RecentCounter()
# print(recentCounter.ping(1))  # Output: 1
# print(recentCounter.ping(100))  # Output: 2
# print(recentCounter.ping(3001))  # Output: 3
# print(recentCounter.ping(3002))  # Output: 3
