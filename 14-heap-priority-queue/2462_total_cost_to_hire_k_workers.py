import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        # Initialize two heaps for the first and last 'candidates' workers
        head = costs[:candidates]
        tail = costs[max(candidates, n - candidates) :]
        heapq.heapify(head)
        heapq.heapify(tail)

        # Initialize pointers for the next elements to be added to the heaps
        next_head = candidates
        next_tail = n - 1 - candidates

        total_cost = 0

        for _ in range(k):
            if not tail or (head and head[0] <= tail[0]):
                # Hire from the head heap
                total_cost += heapq.heappop(head)

                # Add next element to head heap if available
                if next_head <= next_tail:
                    heapq.heappush(head, costs[next_head])
                    next_head += 1
            else:
                # Hire from the tail heap
                total_cost += heapq.heappop(tail)

                # Add next element to tail heap if available
                if next_head <= next_tail:
                    heapq.heappush(tail, costs[next_tail])
                    next_tail -= 1

        return total_cost


# Example usage
# solution = Solution()
# costs = [31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58]
# k = 11
# candidates = 2
# print(solution.totalCost(costs, k, candidates))  # Expected output: 423
