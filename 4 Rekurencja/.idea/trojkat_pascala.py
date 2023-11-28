def Pascal(w,k):
    if k==1:
        return 1
    elif k==w:
        return 1
    else:
        return Pascal(w-1,k-1)+Pascal(w-1,k)

h = int(input('Podaj wysokosc trojkata Pascala: '))
for i in range(1,h+1):
    for j in range(1,h+1):
        if j<=i:
            print(Pascal(i,j), end=' ')
    print()