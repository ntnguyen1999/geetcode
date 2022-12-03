class Solution:
    def maxArea(self, height: List[int]) -> int:
        firstCounter = 0
        lastCounter = len(height)-1
        area = -inf
        while (firstCounter != lastCounter) and (firstCounter != lastCounter - 1):
            if (min(height[firstCounter],height[lastCounter])*(lastCounter - firstCounter)) > area:
                area = min(height[firstCounter],height[lastCounter])*(lastCounter - firstCounter)
            if height[firstCounter] > height[lastCounter]:
                lastCounter -= 1
            else:
                firstCounter += 1
        if (firstCounter == lastCounter - 1):
            if min(height[firstCounter],height[lastCounter]) > area:
                area = min(height[firstCounter],height[lastCounter])
        return area
        
        
        
        