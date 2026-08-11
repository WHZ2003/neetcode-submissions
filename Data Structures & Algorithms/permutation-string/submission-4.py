class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = defaultdict(int)
        appear_set = set()

        count = 0
        target_len = len(s1)

        for c in s1:
            count_s1[c] += 1
            appear_set.add(c)

        count_tmp = count_s1.copy()
        l = 0
        
        for i, c in enumerate(s2):
            if count == target_len:
                return True
            if c in appear_set and count_tmp[c] != 0:
                # print(i)
                count_tmp[c] -= 1
                count += 1
            elif c not in appear_set:
                # deep copy and shallow copy
                count_tmp = count_s1.copy()
                # print(count_tmp)
                count = 0
                l = i + 1
            else:
                # print(count_tmp)
                # print(c,i)
                while count_tmp[c] == 0:
                    count_tmp[s2[l]] += 1
                    l += 1
                    count -= 1

                # add c back
                count_tmp[c] -= 1
                count += 1
                # print(count)


        if count == target_len:
            return True


        return False