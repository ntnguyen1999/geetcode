class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        srtS = "".join(sorted(s))
        srtT = "".join(sorted(t))
        for i in range(0,len(s)):
            if srtS[i] != srtT[i]:
                return False
        return True