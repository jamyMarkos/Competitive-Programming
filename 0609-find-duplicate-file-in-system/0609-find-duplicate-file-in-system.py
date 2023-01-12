class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hash_ = defaultdict(list)
        ans = []
        for path in paths:
            list_ = path.split()
            for i in range(1, len(list_)):
                content = list_[i].split('(')
                temp = ''.join(list_[0] + '/' + content[0])
                hash_[content[1][:-1]].append(temp)
        for content in hash_:
            if len(hash_[content]) >= 2:
                ans.append(hash_[content])
                
        return ans
                
                    
            
            
        