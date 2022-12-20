# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
rooms = list(map(int, input().split()))
Dict = {}

for room_no in rooms:
    if room_no in Dict:
        Dict[room_no] += 1
    else:
        Dict[room_no] = 1

Dict = sorted(Dict.items(), key = lambda x:x[1])
print(Dict[0][0])

        

