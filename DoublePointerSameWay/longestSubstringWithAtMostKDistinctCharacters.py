class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        if len(s) < k:
            return s


        l = r = 0
        start = end = 0

        cnt = 0
        cntS = [0] * 256

        for l in range(len(s)):
            while cnt < k + 1 and r < len(s):
                if cntS[ord(s[r])] == 0:
                    cnt += 1
                cntS[ord(s[r])] += 1
                r += 1

            if cnt == k + 1:
                r -= 1
                cntS[ord(s[r])] -= 1
                cnt -= 1

            if cnt == k:
                if end == 0 or r - l > end - start:
                    start = l; end = r
            
            cntS[ord(s[l])] -= 1
            if (cntS[ord(s[l])]) == 0:
                cnt -= 1
        
        return len(s) if end == 0 else end - start
    
s = Solution()
print(s.lengthOfLongestSubstringKDistinct("aba", 1))