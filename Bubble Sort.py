cnt = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                cnt += 1
                a[i], a[j] = a[j], a[i]
    print("Array is sorted in " + str(cnt) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))
    return a
