def nCr(n,r):
    if r == 0 or n ==r:
        return 1
    return nCr(n-1,r-1) + nCr(n-1,r)
print(nCr(5,2))