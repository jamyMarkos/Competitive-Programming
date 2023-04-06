from collections import defaultdict
def solve():
    n = int(input())

    graph = defaultdict(lambda : [0, 0])
    for i in range(n):
        row = list(map(int, input().split()))
        for idx, val in enumerate(row):
            graph[i+1][0] += val
            graph[idx+1][1] += val

    sinks = [x for x in graph if graph[x][1] and not graph[x][0]]
    sources = [x for x in graph if not graph[x][1] and graph[x][0]]
    tt = [x for x in graph if not graph[x][0] and not graph[x][1]]
    sources.extend(tt)
    sinks.extend(tt)
    
    print(len(sources), *sorted(sources))
    print(len(sinks), *sorted(sinks))
            

if __name__ == '__main__':
    solve()