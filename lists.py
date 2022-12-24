if __name__ == '__main__':
    N = int(input())
    list_ = []
    for i in range(N):
        cmd = list(map(str, input().split(" ")))
        if cmd[0] == "print":
            print(list_)
        elif cmd[0] == 'sort':
            list_.sort()
        elif cmd[0] == 'pop':
            list_.pop()
        elif cmd[0] == 'reverse':
            list_.reverse()
        elif cmd[0] == 'append':
            list_.append(int(cmd[1]))
        elif cmd[0] == 'remove':
            list_.remove(int(cmd[1]))
        else:
            list_.insert(int(cmd[1]), int(cmd[2]))
            
            
