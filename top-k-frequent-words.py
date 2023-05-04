class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        Hash = defaultdict(int)
        for word in words:
            Hash[word] -= 1
        
        heap = []

        for word, neg_count in Hash.items():
            heap.append((neg_count, word))

        heapify(heap)
        ans = []
        for i in range(k):
            ans.append(heappop(heap)[1])

        return ans