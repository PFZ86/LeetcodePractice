# https://leetcode.com/problems/gas-station/

# Solution 1:
# https://leetcode.com/problems/gas-station/discuss/128187/O(n)-time-and-O(1)-space-python-solution-with-new-idea-and-explanation
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        runsum, minidx, minsum = 0, None, None

        for i in range(len(gas)):
            runsum += (gas[i] - cost[i])
            if minsum is None or runsum < minsum:
                minsum = runsum
                minidx = i
        return -1 if runsum < 0 else (minidx+1)%len(gas)
    
