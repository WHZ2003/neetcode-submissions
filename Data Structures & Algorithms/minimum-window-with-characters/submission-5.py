class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = 10000000000
        count_t = defaultdict(int)
        target_len = len(t)
        target_count = 0
        curr_len = 0
        appear_set = set()
        l = 0
        res = ""
        tmp_str = ""
        for c in t:
            count_t[c] += 1
            appear_set.add(c)
        
        for i, c in enumerate(s):
            # print(tmp_str)
            if c not in appear_set and curr_len == 0:
                l += 1
                continue
            elif c not in appear_set and curr_len != 0:
                curr_len += 1
                tmp_str += c
            elif c in appear_set and count_t[c] > 0:
                curr_len += 1
                count_t[c] -= 1
                target_count += 1
                tmp_str += c
            elif c in appear_set and count_t[c] <= 0:
                # add this character first
                curr_len += 1
                count_t[c] -= 1
                tmp_str += c
                # pop unnecessary elements:
                while (count_t[s[l]] < 0 or s[l] not in appear_set) and l < i:
                    # print(s[l], count_t[s[l]])
                    curr_len -= 1
                    # print(tmp_str, curr_len)
                    # print(tmp_str)
                    # if s[l] in appear set and have duplicated, then remove and add count
                    if s[l] in appear_set:
                        count_t[s[l]] += 1
                    
                    tmp_str = tmp_str[1:]
                    l += 1

                # print(count_t)
                # print(tmp_str)

            if(target_len == target_count):
                if (min_len > curr_len):
                    min_len = curr_len
                    res = tmp_str
            
        return res


