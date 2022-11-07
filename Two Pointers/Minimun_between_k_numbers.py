class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        openWindow = 0
        closeWindow = k-1
        minNum = inf
        for i in range(0, len(nums)-k+1):
            if nums[closeWindow] - nums[openWindow] < minNum:
                minNum = nums[closeWindow] - nums[openWindow]
            openWindow+=1
            closeWindow+=1
        return minNum
            