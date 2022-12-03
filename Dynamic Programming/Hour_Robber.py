
class Solution:
    def rob(self, nums: List[int]) -> int:
        prevRob = True
        if len(nums) == 1:
            return nums[0]
        else:
            maxValue = [nums[0],max(nums[0],nums[1])]
            if nums[0] >= nums[1]:
                prevRob = False
            else: prevRob = True
            for i in range(2,len(nums)):
                if prevRob == True:
                    if (nums[i]+maxValue[i-2]) > maxValue[i-1]:
                        prevRob = True
                    else: prevRob = False
                    maxValue.append(max((nums[i]+maxValue[i-2]),maxValue[i-1]))
                else:
                    maxValue.append(nums[i]+maxValue[i-1])
                    prevRob = True
            return maxValue[len(maxValue)-1]