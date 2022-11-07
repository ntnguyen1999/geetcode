class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        firstPointer = 0
        lastPointer = len(s)-1
        if len(s) == 1:
            return s
        else:
            for i in range(int(len(s)/2)):
                temp = s[firstPointer]
                s[firstPointer] = s[lastPointer]
                s[lastPointer] = temp
                firstPointer += 1
                lastPointer -= 1