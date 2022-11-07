class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        firstPointer  = 0
        secondPointer = 1
        sortedNum  = nums.sort()
        if len(nums) == 1:
            return False
        else:
            for i in range(0, len(nums)-1):
                if nums[firstPointer] == nums[secondPointer]:
                    return True
                else:
                    firstPointer += 1
                    secondPointer += 1
            return False


    # time: nlogn, space 1
    # better solution, use hashset while adding value