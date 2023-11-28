from math import floor

print("Podaj wybrany system liczbowy: ", end=' ')
s1=int(input())
print("Podaj liczbe w wybranym systemie: ", end=' ')
liczba=input()
dlugosc=len(liczba)
print("Podaj docelowy system liczbowy: ", end=' ')
s2=int(input())
print("Podana liczba w systemie {}-kowym to: ".format(s2), end=' ')

#zamiana z wybranego na dziesietny
a = 0
while(dlugosc>0):
    for i in liczba:
        alf = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        if i in alf:
            i = alf.index(i) + 10
        a=a+int(i)*(s1**(dlugosc-1))
        dlugosc-=1
        i=str(i)

#zamiana z dziesietnego na docelowy
tablica=[]
while (a>0):
    mod=a%s2

    if (mod>=10):
        alf = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        mod=alf[mod-10]

    a=floor(a/s2)

    tablica.append(mod)

tablica.reverse()

for j in tablica:
    print (j, end='')