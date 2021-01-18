import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = math.sqrt(num)
        if(a > int(a)):
            return False
        else:
            return True
