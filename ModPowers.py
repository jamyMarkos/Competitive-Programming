# Enter your code here. Read input from STDIN. Print output to STDOUT
arr = []
for i in range(3):
    arr.append(int(input()))

[a, b, m] = arr
print(a**b)
print((a**b) % m)
