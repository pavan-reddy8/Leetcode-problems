class Solution:
    def getSum(self, a: int, b: int) -> int:

        if a<0 and b<0:
            a = -a
            b = -b
            return -self.Sum(a,b)
        elif b < 0 and a >= -b:
            return self.Dif(a,-b)
        elif a< 0 and -a > b:
            return -self.Dif(-a,b)
        elif b < 0 and -b > a:
            return  -self.Dif(-b,a)
            
        else:
            return self.Sum(a,b)
    def Sum(self, a: int, b: int) -> int: 
        i = 0
        res = 0
        carry = 0
        while i <=32:
            bita = a & 1
            bitb = b & 1
            # print("a",bin(bita))
            # print("b",bin(bitb))
            a >>= 1
            b >>= 1
            resb = carry ^ bita ^ bitb
            
            if bita == 1 and bitb ==1 or bita == 1 and carry ==1 or carry == 1 and bitb ==1:
                carry = 1
            else:
                carry = 0
            # print(bin(resb),"carry",carry)
            resb = resb << i
            res = res | resb
            i += 1
        return res
    
    def Dif(self, a: int, b: int) -> int: 
        i = 0
        res = 0
        borrow = 0
        while i <=32:
            bita = a & 1
            bitb = b & 1
            print("a",bin(bita))
            print("b",bin(bitb))
            a >>= 1
            b >>= 1
            resb = borrow ^ bita ^ bitb
            
            if bita == 0 and bitb ==1 :
                borrow = 1
            else:
                borrow = 0
            print(bin(resb),"borrow",borrow)
            resb = resb << i
            res = res | resb
            i += 1
        return res
            
            
            
         
        