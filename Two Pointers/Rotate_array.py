from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        queue = deque()
        k = k % len(nums)
        lastPointer = k
        if len(nums)>1:
            for i in range (len(nums)):
                if i < k:
                    queue.append(nums[(lastPointer%len(nums))])
                    nums[(lastPointer%len(nums))] = nums[i]
                    lastPointer += 1
                else:
                    queue.append(nums[(lastPointer%len(nums))])
                    nums[lastPointer%len(nums)] = queue.popleft()
                    lastPointer += 1