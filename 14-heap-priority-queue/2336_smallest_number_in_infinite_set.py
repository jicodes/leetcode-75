import heapq


class SmallestInfiniteSet:
    def __init__(self):
        # Initialize the smallest number in the infinite set
        self.current = 1
        # Min heap to store numbers that have been added back
        self.added = []
        # Set to efficiently check if a number has been added back
        self.addedSet = set()

    def popSmallest(self) -> int:
        if self.added:
            # If we have added-back numbers, the smallest is in the heap
            smallest = heapq.heappop(self.added)
            # Remove from set to maintain consistency
            self.addedSet.remove(smallest)
            return smallest
        else:
            # If no added-back numbers, return current and increment
            self.current += 1
            # Return the original value of current
            return self.current - 1

    def addBack(self, num: int) -> None:
        # Only add back if the number is smaller than current
        # and not already in the added-back set
        if num < self.current and num not in self.addedSet:
            # Add to min heap
            heapq.heappush(self.added, num)
            # Add to set for efficient lookup
            self.addedSet.add(num)
