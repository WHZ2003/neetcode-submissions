class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        m = (n-1) // 2

        res = nums[m]
        itr = 0

        while(l <= r and itr <= 30):
            print(l,r,m)
            if (nums[l] < nums[r]):
                return min(res, nums[l])
            res = min(res,nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
                m = (l + r) // 2
            elif nums[m] < nums[r]:
                r = m - 1
                m = (l + r) // 2
            
            itr += 1


        return res