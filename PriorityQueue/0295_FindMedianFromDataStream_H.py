# https://leetcode.com/problems/find-median-from-data-stream/

# Solution 1: min heap + max heap
'''
maintain len(self.low) = len(self.upp) or len(self.upp) + 1
'''
class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        import heapq
        self.low = []
        self.upp = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.low) == 0 or num <= -self.low[0]:
            heapq.heappush(self.low, -num)
        else:
            heapq.heappush(self.upp, num)

        # maintain len(self.low) = len(self.upp) or len(self.upp) + 1
        if len(self.upp) == (len(self.low) + 1):
            tmp = heapq.heappop(self.upp)
            heapq.heappush(self.low, -tmp)

        if len(self.low) == (len(self.upp) + 2):
            tmp = -heapq.heappop(self.low)
            heapq.heappush(self.upp, tmp)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.low) == len(self.upp):
            return 0.5 * (-self.low[0] + self.upp[0])
        else:
            return -self.low[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
