def is_leap(year):
    leap = False
    
    temp = year / 4
    temp2 = year / 100
    if temp % 2 == 0:
        leap = True
        if temp2 % 2 == 0:
            leap = False
        if year % 400 == 0:
            leap = True   
                
    return leap

year = int(input())
print(is_leap(year))
