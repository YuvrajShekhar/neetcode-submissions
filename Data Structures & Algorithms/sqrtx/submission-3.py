class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 1,x
        while l<=r:
            m = (l+r)//2
            g = self.check_sqr(m,x)
            if g==0:
                return m
            elif g==-1:
                l = m+1
            else:
                r = m-1

        return r

    def check_sqr(self, x:int, target:int) -> int:
        sqr = x*x
        if sqr==target:
            return 0
        elif sqr<target:
            return -1
        else:
            return 1