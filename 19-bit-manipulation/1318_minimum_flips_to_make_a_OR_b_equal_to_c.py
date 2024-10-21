class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0

        for i in range(32):
            bit_a = (a >> i) & 1  # Extract i-th bit of a
            bit_b = (b >> i) & 1  # Extract i-th bit of b
            bit_c = (c >> i) & 1  # Extract i-th bit of c

            if bit_c == 1:
                if bit_a == 0 and bit_b == 0:
                    count += 1  # At least one of a or b needs to be flipped to 1
            else:  # bit_c == 0
                count += (
                    bit_a + bit_b
                )  # Both a and b need to be flipped to 0 if they are 1

        return count
