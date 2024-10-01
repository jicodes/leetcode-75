from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0  # pointer to read through the array
        write = 0  # pointer to write the compressed characters

        while read < len(chars):
            curr_char = chars[read]
            count = 0

            # Count consecutive occurrences of the same character
            while read < len(chars) and chars[read] == curr_char:
                read += 1
                count += 1

            # Write the current character
            chars[write] = curr_char
            write += 1

            # If count > 1, write the count as well
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
