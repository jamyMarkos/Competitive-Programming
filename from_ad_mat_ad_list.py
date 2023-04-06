from collections import defaultdict
def solve():
    nodes = int(input())
    graph = defaultdict(list)
    for i in range(nodes):
        row = map(int, input().split())
        for idx, nbr in enumerate(row):
            if nbr:
                graph[i+1].append(idx+1)
        
        print(len(graph[i+1]), *[str(x) for x in graph[i+1]])


if __name__ == '__main__':
    solve()