class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.stream = []
        self.hash_ = defaultdict(int)
        self.front = 0

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        self.hash_[num] += 1

        if len(self.stream) < self.k:
            return False

        if self.value in self.hash_ and len(self.hash_) == 1:
            tmp = self.stream[self.front]
            self.hash_[tmp] -= 1
            if not self.hash_[tmp]:
                del self.hash_[tmp]
            self.front += 1
            return True
        else:
            tmp = self.stream[self.front]
            self.hash_[tmp] -= 1
            if not self.hash_[tmp]:
                del self.hash_[tmp]
            self.front += 1
            return False


        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)