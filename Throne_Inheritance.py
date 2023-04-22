class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.died = set()
        self.kingName = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.died.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []
        def dfs(cur):
            if cur not in self.died:
                res.append(cur)
            
            for nxt in self.graph[cur]:
                dfs(nxt)
           
        dfs(self.kingName)
        
        return res
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()