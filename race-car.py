class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 1)])
        visit = set() | {(0, 1)}
        lvl = 0
        while q:
            
            for _ in range(len(q)):
                pos, sp = q.popleft()
                if pos == target:
                    return lvl

                # A - accelerate
                if (pos+sp, sp*2) not in visit:
                    q.append((pos+sp, sp*2))
                    visit.add((pos+sp, sp*2))

                # R - reverse
                if (pos, -1 if sp > 0 else 1) not in visit:
                    q.append((pos, -1 if sp > 0 else 1))
                    visit.add((pos, -1 if sp > 0 else 1))
                

            lvl += 1
        
        return -1