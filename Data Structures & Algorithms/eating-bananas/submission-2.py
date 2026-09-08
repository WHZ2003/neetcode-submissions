import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)
        m = (r + l) // 2

        n = len(piles)

        cal_h = 1
        min_k = r

        while (l <= r and m > 0):
            # do inference and find whether is duable

            print(l,r,m)
            cal_h = 0
            for i in range(n):
                cal_h += math.ceil(piles[i] / m)

            if cal_h <= h:
                r = m - 1
                min_k = m
                m = (l+r)//2
            elif cal_h > h:
                l = m + 1
                m = (l+r)//2

        return min_k
