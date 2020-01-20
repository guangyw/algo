from collections import deque

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        subarr = deque()
        arrSum = 0
        if sum(nums) < s:
            return 0
        minLength = len(nums)

        for num in nums:
            subarr.append(num)
            arrSum += num
            while arrSum >= s:
                minLength = min(minLength, len(subarr))
                poped = subarr.popleft()
                arrSum -= poped
        
        return minLength

s = Solution()
s.minSubArrayLen(7, [2,3,1,2,4,3])
            