class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        currPointer = 0
        for i in range (len(nums)):
            if nums[i] != val:
                nums[currPointer] = nums[i] 
                currPointer += 1
        return currPointer