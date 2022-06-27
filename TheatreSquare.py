m, n , a = map(int, input().split())
def theatreSquare(m,n,a):
    if m % a == 0 and n % a == 0:
        temp = (m / a)*(n /a) 
    elif m % a == 0 and n % a != 0:
        temp = (m / a)*( n // a + 1)
    elif m % a != 0  and n % a == 0:
        temp = (m // a + 1)*(n / a)
    else:
        temp = (m // a + 1)*(n // a + 1)
    return int(temp)
print(theatreSquare(m,n,a))
