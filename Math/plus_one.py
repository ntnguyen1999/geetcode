from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        queue = deque()
        remember = False
        for i in range (len(digits)-1,-1,-1):
            if i == len(digits)-1:
                new = digits[i] + 1
                if new == 10:
                    remember = True
                    new = 0
                queue.appendleft(new)
            else: 
                if remember == True:
                    new = digits[i] + 1
                    if new == 10:
                        new = 0
                    else: 
                        remember = False
                    queue.appendleft(new)
                else:
                    queue.appendleft(digits[i])
        if remember == True:
            queue.appendleft(1)            
        return list(queue)