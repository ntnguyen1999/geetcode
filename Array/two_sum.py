class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        hashMap[0] = nums[0]
        for i in range (1,len(nums)):
            findInt = target - nums[i]
            if (findInt) in hashMap.values():
                return [list(hashMap.keys())[list(hashMap.values()).index(findInt)],i]
            else:
                hashMap[i] = nums[i]

## Hash Map