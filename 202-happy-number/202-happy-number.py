class Solution:
    def isHappy(self, n: int) -> bool:
        res = n
        s = {1}
        while True:
            digits = []
            while n:
                digits.append(n % 10)
                n//=10
            for digit in digits:
                n+= digit**2
            if n not in s:
                s.add(n)
            else:
                break
        if n ==1:
            return True
        return False
            