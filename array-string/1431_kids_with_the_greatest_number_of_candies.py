class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # Find the maximum number of candies any kid currently has
        max_candies = max(candies)

        # Use a simplified loop to check each kid's candies
        result = []
        for candy in candies:
            # Check if the current kid will have the greatest number of candies after receiving extraCandies
            result.append(candy + extraCandies >= max_candies)

        return result
