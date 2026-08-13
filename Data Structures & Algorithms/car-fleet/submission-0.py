class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        cur_max = 0
        n = len(position)

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=False)

        for i in range(n - 1, -1, -1):
            s = pair[i][1]
            p = pair[i][0]

            t = (target - p) / s

            if t > cur_max:
                res += 1
                cur_max = t
            
        return res
