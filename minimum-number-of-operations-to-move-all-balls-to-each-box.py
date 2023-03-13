class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        hash_ = defaultdict(list)
        for idx, bit in enumerate(boxes):
            if bit is '1':
                hash_[bit].append(idx)
        list_ = hash_['1']
        for i in range(len(boxes)):
            tmp = 0
            for idx in list_:
                tmp += abs(idx - i)
            res.append(tmp)

        return res