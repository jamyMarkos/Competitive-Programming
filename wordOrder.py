# Enter your code here. Read input from STDIN. Print output to STDOUT

num = int(input())
arr = []
for i in range(num):
    arr.append(input())
Dict = dict()
for string in arr:
    if string in Dict:
        Dict[string] += 1
    else:
        Dict[string] = 1
for key in Dict.values():
    print(key, end=" ")
    
