from collections import defaultdict
def solve():
    n = int(input())
    graph = defaultdict(list)
    for i in range(n):
        row = list(map(int, input().split()))
        for idx, val in enumerate(row):
            if val:
                graph[i+1].append(idx+1)
    ans = 0
    for key, _list in graph.items():
        ans += len(_list)
    print(ans // 2)
  
if __name__ == '__main__':
    solve()