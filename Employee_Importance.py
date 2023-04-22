"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        adjList = {node.id: idx for idx, node in enumerate(employees)}
        visit = set()
        ans = 0
        
        def dfs(cur):
            nonlocal ans
            visit.add(cur)
            ans += employees[adjList[cur]].importance
            for child in employees[adjList[cur]].subordinates:
                if child not in visit:
                    dfs(child)
        
        dfs(id)
            
        return ans
   
