class Solution:
    def reverse(self, n: int) -> int:
        res = 0
        inc = 1

        
        digits = []
        if n <0:
            x =-n
        else:
            x = n
        while x:
            digit = x % 10
            digits.append(digit)
            x//=10

        while digits:
            digit = digits.pop(-1)
            res += digit *inc
            inc*=10
        if  pow(2,31)-1 <= res:
            return 0
        if n<0:
            if  pow(2,-31) <= -res:
                return 0
            return -res
        return res
            
        