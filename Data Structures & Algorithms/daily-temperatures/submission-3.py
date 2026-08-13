class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret = [0] * n
        ret[n-1] = 0
        kept = list()
        kept.append((temperatures[-1], n-1))
        for i in range(n-2, -1, -1):
            # print(kept)
            kept_idx = kept[-1][1]
            kept_temp = kept[-1][0]


            if kept_temp > temperatures[i]:
                ret[i] = kept_idx - i
                kept.append((temperatures[i], i))
            else:
                kept.pop()
                while len(kept) != 0:
                    kept_idx = kept[-1][1]
                    kept_temp = kept[-1][0]

                    if kept_temp > temperatures[i]:
                        ret[i] = kept_idx - i
                        kept.append((temperatures[i], i))
                        break
                    else:
                        kept.pop()
                if len(kept) == 0:
                    ret[i] = 0
                    kept.append((temperatures[i], i))


        
        return ret