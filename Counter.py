# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
def userInput():
    N = int(input())
    list_ = [] * N
    list_ = list(map(int, input().split()))
    return Counter(list_)

if __name__== '__main__':
    numInShoe = userInput()
    netSell = 0
    X = int(input())
    for _ in range(X):
        size, price = map(int, input().split())
        if numInShoe[size] >= 1:
            netSell += price
            numInShoe[size] -= 1
    print(netSell)
            
