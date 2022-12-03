class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        firstCounter = 0
        if len(s) == 0:
            return True
        else:
            for i in range (len(t)):
                if t[i] == s[firstCounter]:
                    firstCounter += 1
                    if firstCounter == len(s):
                        return True
        return False
