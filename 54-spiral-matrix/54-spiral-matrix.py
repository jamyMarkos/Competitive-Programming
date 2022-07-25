class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(matrix), len(matrix[0])
        tot = m * n
        i = 0
        while len(ans) < tot:
            j = i
            while len(ans) < tot and j < n:
                ans.append(matrix[i][j])
                j += 1
            k = i + 1
            while len(ans) < tot and k < m:
                ans.append(matrix[k][n-1])
                k += 1
            l = n - 2
            while len(ans) < tot and l >= i:
                ans.append(matrix[m-1][l])
                l -= 1
            o = m-2
            while len(ans) < tot and o > i:
                ans.append(matrix[o][i])
                o -= 1
            i += 1
            n -= 1
            m -= 1
        return ans
                    
                
                
        