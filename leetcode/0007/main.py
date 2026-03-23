class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        result = 0
        if x < 0:
            x = -x
            sign = -1
        while x != 0:
            result = result * 10 + x % 10
            x = x // 10
        result *= sign
        if result < -2**31 or result > 2**31-1:
            return 0
        return result
