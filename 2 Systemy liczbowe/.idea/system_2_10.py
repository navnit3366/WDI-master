print("Podaj liczbe w systemie binarnym: ", end=' ')
liczba_bin=input()
dlugosc=int(len(liczba_bin))
a=0

while(dlugosc>0):
    for i in liczba_bin:
        a=a+int(i)*(2**(dlugosc-1))
        dlugosc-=1
        i=str(i)
print("Podana liczba w systemie dziesietnym to: ", a)