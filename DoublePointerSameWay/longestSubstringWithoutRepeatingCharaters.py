from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        arr = deque()
        maxLen = 0

        for c in s:
            while c in charSet:
                poped = arr.popleft()
                charSet.remove(poped)

            arr.append(c)
            charSet.add(c)
            maxLen = max(maxLen, len(arr))
        
        return maxLen

s = Solution()
s.lengthOfLongestSubstring("abcabcbb")
