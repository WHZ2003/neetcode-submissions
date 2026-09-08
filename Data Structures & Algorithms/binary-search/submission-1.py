class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        m = (n-1) // 2
        l = 0
        r = n -1
        itera = 0 
        while (l <= r and itera < 20):
            print(l, m, r)
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1
                m = (r+l)//2
            else:
                l = m + 1
                m = (r+l)//2
            
            
            itera += 1

        return -1