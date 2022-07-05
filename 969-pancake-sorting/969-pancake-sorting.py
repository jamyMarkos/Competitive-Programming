class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        y = len(arr) 
        answer = []
        def flip(ary: list[int],flag)-> list[int]:
            start = 0
            while start < flag:
                ary[start], ary[flag] = ary[flag], ary[start]
                start += 1
                flag -= 1
            return ary
        while y > 1:
            flag = indexOf(arr, max(arr[:y]))
            if flag == y - 1:
                y -= 1
                continue
            elif flag == 0:
                arr[:y] = flip(arr[:y], y-1)
                answer.append(y)
            else:
                arr[:flag+1] = flip(arr[:flag+1], flag)
                answer.append(flag+1)
                arr[:y] = flip(arr[:y], y-1)
                answer.append(y)
            y -= 1
        return answer

        
        