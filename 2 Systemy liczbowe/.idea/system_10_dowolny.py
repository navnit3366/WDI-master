from math import floor

print("Podaj liczbe w systemie dziesietnym: ", end=' ')
liczba_dec=int(input())

print("Podaj docelowy system liczbowy: ", end=' ')
system=int(input())

print("Podana liczba w systemie {}-kowym to: ".format(system), end=' ')

tablica=[]

while (liczba_dec>0):
    mod=liczba_dec%system

    if (mod>=10):
        alf="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        mod=alf[mod-10]

    liczba_dec=floor(liczba_dec/system)

    tablica.append(mod)

tablica.reverse()

for i in tablica:
    print (i, end='')