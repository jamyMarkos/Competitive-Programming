class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashTable = {letter: idx + 1 for idx, letter in enumerate(order)}
        
        for i in range(len(words) - 1):
            ptr1, ptr2 = 0, 0
            while ptr1 < len(words[i]) and ptr2 < len(words[i+1]):
                if hashTable[words[i][ptr1]] < hashTable[words[i+1][ptr2]]:
                    break
                elif hashTable[words[i][ptr1]] > hashTable[words[i+1][ptr2]]: 
                    return False
                ptr1 += 1
                ptr2 += 1
            else:
                if words[i][ptr1-1] == words[i+1][ptr2-1]:
                    if len(words[i]) <= len(words[i+1]):
                        continue
                    else:
                        return False
        
                
        return True
        