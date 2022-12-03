class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        firstIndex = 0
        lastIndex = len(numbers)-1
        numberFound = False
        while numberFound == False:
            if target - numbers[firstIndex] < numbers[lastIndex]:
                lastIndex -= 1
            elif target - numbers[firstIndex] > numbers[lastIndex]:
                firstIndex += 1
            else:
                numberFound = True
        return[firstIndex+1,lastIndex+1]