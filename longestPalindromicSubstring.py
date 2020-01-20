class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if not s:
            return ""
        res = ""
        for i in range(len(s)):
            pal = self.findPalindrome(s, i, i)
            if len(pal) > len(res):
                res = pal
            pal = self.findPalindrome(s, i, i+1)
            if len(pal) > len(res):
                res = pal
        return res 

    def findPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l + 1:r]
        

    def longestPalindromeDp(self, s):
        if not s:
            return ""

        n = len(s)
        is_palindrom = [[False] * n for _ in range(n)]
        is_palindrom[0][0] = True
        for i in range(len(s)):
            is_palindrom[i][i] = True
            # This idx is easy to mess up. 
            # With the below check is_palindrom[i+1][j-1], i would be smaller than j, when it comes to single element str
            is_palindrom[i][i-1] = True

        start, longest = 0, 1
        for length in range(2, n + 1):
            for i in range(n -length + 1):
                j = i + length -1
                is_palindrom[i][j] = is_palindrom[i+1][j-1] and s[i] == s[j]
                
                if is_palindrom[i][j] and length > longest:
                    start = i
                    longest = length 
        
        return s[start:start + longest]

s = Solution()
s.longestPalindromeDp("cbbd")
