class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for i in range(len(nums)):
            # push the current val to heap
            heapq.heappush(heap, (-nums[i], i))
            # if this val exceed the window size, then update
            if i >= k - 1:
                # pop the greatest number until the number is still in the window
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output