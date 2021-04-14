class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        elif x > 0:
            a = str(x)
            # int_max
            if int(a[::-1]) < 2147483647:
                return (int(a[::-1]))
            else:
                return 0
        else:
            a = str(x)
            a = a[1:]
            # int_min
            if (-int(a[::-1])) > -2147483648:
                return (-int(a[::-1]))
            else:
                return 0