# https://leetcode.com/problems/two-city-scheduling/

# Solution 1: sort by cost_diff
import numpy as np
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        num_people = len(costs)
        cost_diffs = np.zeros(num_people)
        for i in range(num_people):
            cost_diffs[i] = costs[i][0] - costs[i][1]
        tmp = np.argsort(cost_diffs)
        total_cost = 0
        # first half to A
        for i in tmp[:num_people/2]:
            total_cost += costs[i][0]
        # second half to B
        for i in tmp[num_people/2:]:
            total_cost += costs[i][1]

        return total_cost
