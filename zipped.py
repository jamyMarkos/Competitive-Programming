# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    N, X = map(int, input().split())
    subList = []
    for sum in range(X):
        subList.append(list(map(float, input().split(" "))))

    Y = []
    for llist in subList:
        Y += [llist]
    
    for stuScore in zip(*Y):
        temp = 0
        for el in stuScore:
            temp += el
        print(round(temp / X, 1))       
