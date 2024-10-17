class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # Stack to hold numbers and strings
        curr_num = 0  # Current number (k)
        curr_str = ""  # Current decoded string

        for char in s:
            if char.isdigit():  # Build the current number
                curr_num = curr_num * 10 + int(char)
            elif char == "[":  # Push current state onto stack
                stack.append((curr_str, curr_num))
                curr_str, curr_num = "", 0  # Reset for new context
            elif char == "]":  # Pop from stack and decode
                last_str, k = stack.pop()
                curr_str = last_str + curr_str * k  # Repeat and concatenate
            else:  # Add to current string
                curr_str += char

        return curr_str  # Final decoded string


# Example usage:
# solution = Solution()
# print(solution.decodeString("3[a2[c]]"))  # Output: "accaccacc"
