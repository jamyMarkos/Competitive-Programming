class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        monoStack = []
        hash_map = Counter(s)
        count = defaultdict(int)
        # hash_cmp = defaultdict(int)

        for letter in s:
            if not monoStack:
                monoStack.append(letter)
                count[letter] += 1
            elif count[letter] < 1:
                while monoStack and letter < monoStack[-1] and hash_map[monoStack[-1]] > 1:
                    popped = monoStack.pop()
                    count[popped] -= 1
                    hash_map[popped] -= 1
                    
                monoStack.append(letter)
                count[letter] += 1
            else:
                hash_map[letter] -= 1


        return ''.join(monoStack)