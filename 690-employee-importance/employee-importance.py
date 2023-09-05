"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        
        employee_data = {employee.id: employee for employee in employees}
        
        def dfs(employee_id):
         
            employee = employee_data[employee_id]
         
            total_imp = employee.importance
            
          
            for subordinate in employee.subordinates:
                total_imp += dfs(subordinate)
            
            return total_imp
        
       
        return dfs(id)
        