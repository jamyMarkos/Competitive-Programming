# Compare the sizes of T-shirt

if __name__ == '__main__':
    hash_ = {
        'S' : 0,
        'M' : 1,
        'L' : 2
        }
    comp = int(input())
    for i in range(comp):
        a, b = input().split()
        if a == b: print('=')
        elif hash_[a[-1]] > hash_[b[-1]]:
            print('>')
        elif hash_[a[-1]] < hash_[b[-1]]:
            print('<')
        elif hash_[a[-1]] == hash_[b[-1]] and a[-1] == 'S':
            print( '<' if len(a) > len(b) else '>')
        elif hash_[a[-1]] == hash_[b[-1]] and a[-1] == 'L':
            print( '>' if len(a) > len(b) else '<')
        
