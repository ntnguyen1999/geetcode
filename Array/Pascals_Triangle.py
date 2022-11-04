class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        currRow = 1
        currArray =[]
        returnArr = []
        for i in range(1,numRows+1):
            if currRow == 1:
                currArray = [1]
                returnArr.append(currArray)
                currRow += 1
            elif currRow == 2:
                currArray = [1,1]
                returnArr.append(currArray)
                currRow += 1
            else:
                firstPointer = 0
                secondPointer = 1
                newArray = []
                newArray.append(1)
                for i in range(len(currArray) - 1):
                    newArray.append(currArray[firstPointer] + currArray[secondPointer])
                    firstPointer += 1
                    secondPointer += 1
                newArray.append(1)
                returnArr.append(newArray)
                currArray = newArray
                currRow += 1
        return returnArr