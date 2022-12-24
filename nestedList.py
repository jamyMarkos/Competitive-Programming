from collections import defaultdict
if __name__ == '__main__':
    dict_ = defaultdict(list)
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dict_[score].append(name)
    dict_ = sorted(dict_.items())
    dict_[1][1].sort()
    for names in dict_[1][1]:
        print(names)
    
        
            
            
        
