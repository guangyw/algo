import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # v & 1 to get odd numbers
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)

s = Solution()
s.longestPalindrome("abbbcccc")
            