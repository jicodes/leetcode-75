class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenation of str1 and str2 is equal in both orders
        if str1 + str2 != str2 + str1:
            return ""

        # Calculate GCD of the lengths using our own implementation
        gcd_length = self.gcd(len(str1), len(str2))

        # Return the substring of length gcd_length
        return str1[:gcd_length]

    def gcd(self, a: int, b: int) -> int:
        # Euclidean algorithm for GCD
        while b:
            a, b = b, a % b
        return a
