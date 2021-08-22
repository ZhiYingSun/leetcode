class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:                                   # base case
            return True
        else:
            return n % 2 == 0 and self.isPowerOfTwo(n/2)    # every n is divisible by 2 and n/2 is power of two
        