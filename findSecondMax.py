from typing import List
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # def removeR(arr: List[int])-> List[int]:
    #     ans = [x for x in arr if x not in ans]
    #     return ans.sort()
    # arr2 = arr.sort(key=removeR)
    # print(arr2[-2])
    arr.sort(reverse=True)
    
    temp = 0
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            print(arr[i+1])
            break
        
            
