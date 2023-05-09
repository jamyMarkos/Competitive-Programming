class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indeg = defaultdict(int)

        for idx, el in enumerate(recipes):
            for i, ing in enumerate(ingredients[idx]):
                graph[ing].append(el)

            indeg[el] = len(ingredients[idx])

        q = deque()

        for el in supplies:
            if indeg[el] == 0:
                q.append(el)
           
        order = []
        while q:
            cur = q.popleft()
            if cur in recipes:
                order.append(cur)
            for nbr in graph[cur]:
                indeg[nbr] -= 1
                if indeg[nbr] == 0:
                    q.append(nbr)
                    
        return order