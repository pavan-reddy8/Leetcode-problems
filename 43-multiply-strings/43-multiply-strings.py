class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1)+len(num2))
        ress = ""
        for i in range(len(num2)):
            for j in range(len(num1)):
                digit = int(num2[i]) * int(num1[j])
                res[i+j] += digit
                res[i+j+1] += (res[i+j]//10) 
                res[i+j] = res[i+j]%10
                # print(res)
        while res[-1] == 0:
            res.pop(-1)
        print(res)
        while res:
            ress += str(res.pop(-1))
        return ress
        