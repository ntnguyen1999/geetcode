class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list = []
        list[:0] = s
        inWord = False
        firstPointer = 0
        lastPointer = 0
        for i in range (len(list)):
            if (inWord == False):
                if list[i] != ' ':
                    if (i == len(list)-1)or(list[i+1] == ' '):
                        firstPointer = i
                        lastPointer = i
                    else:
                        firstPointer = i
                        inWord = True
            else:
                if (list[i] != ' ' and i == (len(list)-1)) or (list[i] != ' ' and list[i + 1] == ' '):
                    lastPointer = i
                    inWord = False
        return lastPointer - firstPointer + 1
                    
                        