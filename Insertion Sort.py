val = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > val:
            arr[i+1] = arr[i]
            print(" ".join(map(str, arr)))
        else:
            arr[i+1] = val
            print(" ".join(map(str, arr)))
            break
    if arr[0] > val:
        arr[0] = val
        print(" ".join(map(str, arr)))
