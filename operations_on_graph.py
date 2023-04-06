from collections import defaultdict
def solve():
    n = int(input())
    graph = defaultdict(list)

    k = int(input())

    for _ in range(k):
        op = list(map(int, input().split()))
        if op[0] == 1:
            graph[op[1]].append(op[2])
            graph[op[2]].append(op[1])
        else:
            if graph[op[1]]:
                print(*graph[op[1]])



if __name__ == '__main__':
    solve()