#Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
#Example:
#
#Input: S = "ADOBECODEBANC", T = "ABC"
#Output: "BANC"
#Note:
#
#If there is no such window in S that covers all characters in T, return the empty string "".
#If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

class Solution:
    def minWindow(self, s, t):

        cntS = [0] * 256
        cntT = [0] * 256

        pStart = 0
        pEnd = 0

        uniqueCnt = 0
        for c in t:
            if not cntT[ord(c)]:
                uniqueCnt += 1
            cntT[ord(c)] += 1
        
        i = j = 0

        totalCnt = 0
        for i in range(len(s)):
            while j < len(s) and totalCnt < uniqueCnt:
                cntS[ord(s[j])] += 1
                if cntS[ord(s[j])] == cntT[ord(s[j])]:
                    totalCnt += 1
                j += 1
            
            if totalCnt == uniqueCnt:
                if pEnd == 0 or j - i < pEnd - pStart:
                    pEnd = j; pStart = i
            
                cntS[ord(s[i])] -= 1
                if cntS[ord(s[i])] < cntT[ord(s[i])]:
                    totalCnt -= 1

                i += 1
            else:
                break
        
        
        return s[pStart: pEnd]