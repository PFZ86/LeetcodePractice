# https://leetcode.com/problems/sliding-window-maximum/

# Solution 1: maintain a deque of index
#             delete from front old elements
#             delete from back small elements
'''
nums = [1,3,-1,-3,5,3,6,7], and k = 3
idx     num     idx_queue     (num_queue)            res
  0       1             0               1
  1       3             1               3
  2      -1           1,2            3,-1              3
  3      -3         1,2,3         3,-1,-3            3,3
  4       5             4               5          3,3,5
  5       3           4,5             5,3        3,3,5,5
  6       6             6               6      3,3,5,5,6
  7       7             7               7    3,3,5,5,6,7
'''

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        idx_queue = []
        res = []
        for idx, num in enumerate(nums):
            # delete from front: remove elements at least k positions before idx
            while len(idx_queue) and idx_queue[0] <= (idx-k):
                del idx_queue[0]
            # delete from back: remove elements no greater than num
            while len(idx_queue) and nums[idx_queue[-1]] <= num:
                del idx_queue[-1]
            # add current index
            idx_queue.append(idx)

            if idx >= (k-1):
                res.append(nums[idx_queue[0]])

        return res
