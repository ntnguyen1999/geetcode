from collections import deque
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        queue = deque()
        maxNum = 0
        for i in range (len(arr)-1,-1,-1):
            if i == len(arr)-1:
                maxNum = arr[i]
                queue.appendleft(-1)
            else:
                queue.appendleft(maxNum)
                if arr[i] > maxNum:
                    maxNum = arr[i]
        return list(queue)