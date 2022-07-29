class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 0
        for i in range(len(digits)-1,-1,-1):
            # print(digits[i])
            # print(res)
            ans = 0
            if i == len(digits)-1:
                ans = digits[i] + 1
            else:
                ans = carry + digits[i]
            digit = ans %10
            carry = ans//10
            res.append(digit)
        if carry:
            res.append(carry)
        res.reverse()
        return res

            
            
        