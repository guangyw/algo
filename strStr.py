class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLen = len(needle)
        for i in range(len(haystack) - needleLen + 1):
            if haystack[i:i + needleLen] == needle:
                return i
            
        return -1
                
s = Solution()
s.strStr("hello", "ll")