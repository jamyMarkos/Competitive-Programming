# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    arr = []
    ans = False
    setA = set(map(int, input().split()))
    n = int(input())
    for _ in range(n):
        arr.append(set(map(int, input().split())))
    
    for set_ in arr:
        if set_.issubset(setA):
            if len(set_) < len(setA):
                ans = True
        else:
            ans = False
            break
                
    print(ans)
        
    
