class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        # Step 1: Process each character in the string
        for char in s:
            if char != "*":
                stack.append(char)  # Add character to stack
            else:
                stack.pop()  # Remove last character for each '*'

        # Step 2: Join the stack to form the final result
        return "".join(stack)
