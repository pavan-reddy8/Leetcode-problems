class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l , r = 0, 0
        res = 0
        basket = defaultdict(int)
        while r < len(fruits):
            basket[fruits[r]]+=1
            
            while len(basket) > 2:
                basket[fruits[l]] -=1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l+=1
            res = max(res,r-l+1)
            r+=1
               
        return res