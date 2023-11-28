tab_liczb_doskonalych = []

for i in range(2,10001):
    tab_dzielnikow = []
    for j in range(1,i):
        if i%j==0:
            tab_dzielnikow.append(j)
    length = len(tab_dzielnikow)
    suma_elementow_tab = 0
    for k in range(length):
        suma_elementow_tab += tab_dzielnikow[k]
    if suma_elementow_tab == i:
        tab_liczb_doskonalych.append(i)

print(tab_liczb_doskonalych)