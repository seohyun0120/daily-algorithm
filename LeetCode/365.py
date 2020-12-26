class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        def gcd(a, b):
            print(a,b)
            while b:
                a, b = b, a%b
            return a

        if (x == z or y == z or x + y == z):
            return True
        
        if (x + y < z):
            return False

        if (z % gcd(x,y) == 0):
            return True