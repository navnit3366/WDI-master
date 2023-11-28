import random

tab = []
for i in range(50):
    tab.append(random.randint(1,100))
print(tab)

#BUBBLE
tab_bub = tab
sorted = False
while not sorted:
    sorted = True
    for i in range(49):
        if tab_bub[i]>tab_bub[i+1]:
            sorted = False
            tmp = tab_bub[i]
            tab_bub[i] = tab_bub[i+1]
            tab_bub[i+1] = tmp
print(tab_bub)

#SELECT
tab_sel = tab
for j in range(49):
    min = j
    for i in range(j+1,50):
        if tab_sel[min]>tab_sel[i]:
            min = i
    tmp = tab_sel[min]
    tab_sel[min] = tab_sel[j]
    tab_sel[j] = tmp
print(tab_sel)

#INSERT
tab_ins = tab
for i in range(1,50):
    a = i-1
    while a>=0:
        if tab[i]<tab[a]:
            tab[i], tab[a] = tab[a], tab[i]
        a -= 1
print(tab_ins)