# Enter your code here. Read input from STDIN. Print output to STDOUT
x, y = map(int, input().split())
# input()
llist = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happiness = 0

for i in llist:
    if i in a:
        happiness += 1
    if i in b:
        happiness -= 1

print(happiness)
        

