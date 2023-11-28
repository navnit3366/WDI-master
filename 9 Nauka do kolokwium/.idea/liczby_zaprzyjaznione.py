tab_liczb_zaprzyjaznionych = []

for i in range(1,3000):
    tab_dzielnikow = []
    for j in range(1, i):
        if i%j==0:
            tab_dzielnikow.append(j)
    length = len(tab_dzielnikow)
    suma_dzielnikow = 0
    for k in range(length):
        suma_dzielnikow += tab_dzielnikow[k]

    tab_dzielnikow2 = []
    for m in range(1, suma_dzielnikow):
        if suma_dzielnikow % m == 0:
            tab_dzielnikow2.append(m)
    length2 = len(tab_dzielnikow2)
    suma_dzielnikow2 = 0
    for n in range(length2):
        suma_dzielnikow2 += tab_dzielnikow2[n]
    if suma_dzielnikow2 == i and suma_dzielnikow!=i:
        tab_liczb_zaprzyjaznionych.append(i)

o = 0
for p in tab_liczb_zaprzyjaznionych:
    if o%2!=0:
        print(p)
    else:
        print(p, end=' ')
    o+=1