class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 永远对短数组二分
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        left, right = 0, m

        while left <= right:
            # nums1 左边放 i 个
            i = (left + right) // 2

            # nums2 左边必须放 j 个
            j = (m + n + 1) // 2 - i

            left1 = float("-inf") if i == 0 else nums1[i - 1]
            right1 = float("inf") if i == m else nums1[i]

            left2 = float("-inf") if j == 0 else nums2[j - 1]
            right2 = float("inf") if j == n else nums2[j]

            # 找到了正确 partition
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))

                return (
                    max(left1, left2) +
                    min(right1, right2)
                ) / 2

            # nums1 切得太靠右
            elif left1 > right2:
                right = i - 1

            # nums1 切得太靠左
            else:
                left = i + 1