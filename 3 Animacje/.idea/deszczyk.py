import random

size = int(input('Podaj rozmiar nieba: '))

#poczatkowa tablica kropli w size-1 wierszach
raindrops = []
for i in range(size-1):
    a = random.randint(0,size-1)
    raindrops.insert(0,a)

for k in range(5):
    a = random.randint(0,size-1)
    raindrops.insert(0,a)
    for i in range(size):
        for j in range(size):
            if raindrops[i] == j:
                print('o', end=' ')
            else:
                print('.', end=' ')
        print()
    print()
    raindrops.pop(size-1)