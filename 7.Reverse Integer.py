class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        d = 1
        str_x = str(x)
        neg = False
        for i in str_x:
            if i is '-':
                neg = True
                continue
            n = int(i)
            result += d * n
            d *= 10

        if neg:
            result = -1 * result

        if abs(result) > 2147483647:
            return 0

        return result
