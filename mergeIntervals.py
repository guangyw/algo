"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, a):
        # write your code here
        a.sort(key = lambda interval: interval.start)

        ans = []
        prev = None
        for interval in a:
            if prev == None or prev.end < interval.start:
                ans.append(interval)
                prev = interval
            else:
                prev.end = max(prev.end, interval.end)
        
        return ans