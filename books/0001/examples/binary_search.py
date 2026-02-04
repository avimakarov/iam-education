def bsearch(arr, v):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0 if arr[0] == v else -1
    
    l = 0
    u = len(arr) - 1

    while l <= u:
        m = (l + u) // 2
        if arr[m] == v:
            return m
        
        if v < arr[m]:
            u = m - 1
        else:
            l = m + 1
    
    return -1

if __name__ == "__main__":
    print(bsearch([i for i in range(100, 10000)], 444))

