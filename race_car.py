class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 1)])
        count = 0
        visit = set([(0, 1)])
        while q:
            for i in range(len(q)):
                pos, speed = q.popleft()
                if pos == target:
                    return count
                
                for inst in ['A', 'R']:
                    if inst == 'A':
                        if (pos+speed, speed*2) not in visit:
                            q.append((pos+speed, speed*2))
                            visit.add((pos+speed, speed*2))
                    if inst == 'R':
                        if speed > 0 and (pos, -1) not in visit:
                            q.append((pos, -1))
                            visit.add((pos, -1))
                        elif speed <= 0 and (pos, 1) not in visit:
                            q.append((pos, 1))
                            visit.add((pos, 1))

            count += 1
    
        