from math import ceil

size = int(input('Podaj rozmiar kwadracika: '))

half = ceil(size/2)

for k in range(half):
    for i in range(size):
        for j in range(size):
            #pierwsza czesc to warunki otaczajace kwadrat od zewnatrz, druga rysujace serduszka w odpowiednich miejscach
            if (i>=k and i<=size-1-k and j>=k and j<=size-1-k) and (i==k or j==k or i==size-1-k or j==size-1-k):
                print('♥', end=' ')
            else:
                print('.', end=' ')
        print()
    print()