from collections import  defaultdict    

def solve():

    while True:
        n = int(input())
        if not n:
            return

        l = int(input())
        graph = defaultdict(list)
        colors = defaultdict(int)
        # construct the graph
        for _ in range(l):
            a, b = list(map(int, input().split()))
            graph[a].append(b)
            graph[b].append(a)

        # depth first search
        def dfs(vertex):
            for nbr in graph[vertex]:
                # already colored...
                if nbr in colors:
                    if colors[nbr] == colors[vertex]:
                        return False
                else:
                    # not colored...
                    colors[nbr] = 3 - colors[vertex]
                    if not dfs(nbr):
                        return False
            return True
        
        flag = True
        for vertex in graph:
            if vertex not in colors:
                colors[vertex] = 1
                if not dfs(vertex):
                    print('NOT BICOLOURABLE.')
                    flag = False
                    break
                    
        if flag:
            print('BICOLOURABLE.')

if __name__ == '__main__':
    solve()