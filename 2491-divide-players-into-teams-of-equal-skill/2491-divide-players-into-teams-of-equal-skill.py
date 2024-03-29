class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill) - 1
        chemistry = 0
        sum_ = skill[left] + skill[right]
        while left < right:
            if skill[left] + skill[right] != sum_:
                return -1
            chemistry += (skill[left] * skill[right])
            left += 1
            right -= 1
            
        return chemistry
            
            
        