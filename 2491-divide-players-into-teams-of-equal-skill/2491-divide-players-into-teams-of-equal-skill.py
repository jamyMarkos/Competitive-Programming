class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = []
        skill.sort()
        left, right = 0, len(skill) - 1
        sum_ = skill[left] + skill[right]
        while left < right:
            if skill[left] + skill[right] != sum_:
                return -1
            res.append([skill[left], skill[right]])
            left += 1
            right -= 1
            
        chemistry = 0
        for pair in res:
            chemistry += (pair[0] * pair[1])
        return chemistry
            
            
        