# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(input())
ordDict = OrderedDict()
for _ in range(N):
    str_ = input().split(" ")
    name = " ".join(str_[:-1])
    price = int(str_[-1])
    if name in ordDict:
        ordDict[name] += price
    else:
        ordDict[name] = price 
        
for item_sold in ordDict:
    print(item_sold, ordDict[item_sold])
