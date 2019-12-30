# https://leetcode.com/problems/employee-importance/

"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

# Solution 1:
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: [Employee]
        :type id: int
        :rtype: int
        """
        id_to_idx = {}
        for idx, employee in enumerate(employees):
            id_to_idx[employee.id] = idx

        id_visited = {}
        total_importance = 0
        id_queue = [id]

        while len(id_queue):
            employee_id = id_queue[0]
            del id_queue[0]
            if employee_id in id_visited:
                continue
            id_visited[employee_id] = 1
            employee = employees[id_to_idx[employee_id]]
            total_importance += employee.importance
            for subordinate_id in employee.subordinates:
                id_queue.append(subordinate_id)

        return total_importance
        
