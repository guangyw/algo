#Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.
#
#If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.
#
#Example 1:
#
#Input: 
#S = "abcdebdde", T = "bde"
#Output: "bcde"
#Explanation: 
#"bcde" is the answer because it occurs before "bdde" which has the same length.
#"deb" is not a smaller window because the elements of T in the window must occur in order.
 #
#
#Note:
#
#All the strings in the input will only contain lowercase letters.
#The length of S will be in the range [1, 20000].
#The length of T will be in the range [1, 100].

class Solution:
    # time limit exceeded
    def minWindow(self, S: str, T: str) -> str:
        
        l = r = 0
        i = 0
        start = 0
        end = 0

        for l in range(len(S)):
            if S[l] == T[0]:
                tmp = l
                while tmp < r:
                    if S[tmp] == T[i]:
                        i += 1
                    tmp += 1

                while i < len(T) and r < len(S):
                    if S[r] == T[i]:
                        i += 1
                    
                    r += 1
                
                if i == len(T):
                    if end == 0 or r - l < end - start:
                        start = l; end = r
                
                i = 0
        
        return S[start:end]

    # time limit exceeded
    def minWindowWithReverseCheck(self, S: str, T: str) -> str:
        l = r = i = 0
        start = end = 0

        while l < len(S):
            if S[l] == T[0]:
                while i < len(T) and r < len(S):
                    if S[r] == T[i]:
                        i += 1
                    r += 1
                
                if i == len(T):
                    l = r - 1
                    i = i - 1

                    while i >= 0:
                        if S[l] == T[i]:
                            i -= 1
                        l -= 1
                    l += 1

                    if end == 0 or r - l < end - start:
                        start = l; end = r
            
            l += 1
            r = l
        
        return S[start:end]

s = Solution()
s.minWindowWithReverseCheck("abcdebdde", "bde")
