#User function Template for python3

class Solution: 
    def select(self, arr, i):
        min_ = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_]:
                min_ = j
        return min_
       
            
            
    
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            min_idx = self.select(arr, i)
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
        
        return arr
            
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
