from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []  # No digits, return empty list

        # Mapping of digits to corresponding letters
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []  # Store the result combinations

        # Backtracking function to build combinations
        def backtrack(index, curr_comb):
            if index == len(digits):  # If we've processed all digits
                result.append("".join(curr_comb))  # Add current combination to result
                return

            # Get the letters corresponding to the current digit
            letters = phone_map[digits[index]]
            for letter in letters:
                curr_comb.append(letter)  # Add the letter to the current combination
                backtrack(index + 1, curr_comb)  # Recurse to process the next digit
                curr_comb.pop()  # Backtrack by removing the last added letter

        # Start backtracking from the first digit
        backtrack(0, [])

        return result


# Time: O(4^n), where n is the length of the input digits string (since each digit can map to up to 4 letters).
# Space: O(n), where n is the depth of the recursion stack and the space used to store the combinations.
