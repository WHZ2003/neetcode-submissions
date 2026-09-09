class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1


        while (l <= r):
            m = (l + r) // 2
            print(l, r, m)
            if (nums[m] == target):
                return m


            if (target > nums[m]):
                # rot
                if (nums[m] > nums[n-1]):
                    l = m + 1
                # unrot
                else:
                    # unrot
                    if (target <= nums[n-1]):
                        l = m + 1
                    # rot
                    else:
                        r = m - 1
            else:
                # unrot
                if nums[m] > nums[n-1]:
                    if target <= nums[n-1]:
                        l = m + 1
                    else:
                        r = m - 1

                # rot
                else:
                    r = m - 1


        
        return -1
