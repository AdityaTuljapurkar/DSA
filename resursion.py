class Solution :
    def function(self, num: int, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return  num 
        else : 
            val = self.function(num, n//2)
            ans = val * val
            if n % 2 != 0:
                return ans *num 
           
            return ans 
print(Solution().function(2, 10))
        