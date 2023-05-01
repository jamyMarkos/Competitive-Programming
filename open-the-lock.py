class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit = set(deadends)
        if '0000' in visit:
            return -1
        if target == '0000':
            return 0

        visit.add('0000')
        q = deque(['0000'])
        lvl = 0
        while q:
            lvl += 1
            for _ in range(len(q)):
                key = list(map(int, q.popleft()))
                for i in range(4):
                    key[i] = (key[i] + 1) % 10
                    tt = ''.join(map(str,key))
                    if tt not in visit:
                        q.append(tt)
                        visit.add(tt)
                    
                    if target == tt:
                        return lvl
                    
                    key[i] = (key[i]-2) % 10
                    tt = ''.join(map(str, key))
                    if tt not in visit:
                        q.append(tt)
                        visit.add(tt)
                    
                    if target == tt:
                        return lvl

                    key[i] = (key[i]+1) % 10


        return -1