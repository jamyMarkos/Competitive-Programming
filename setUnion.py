# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    Eng_sub = int(input())
    list_e = set(list(map(int, input().split())))
    Fre_sub = int(input())
    list_f = set(list(map(int, input().split())))
    
    print(len(list_e.union(list_f)))
    
