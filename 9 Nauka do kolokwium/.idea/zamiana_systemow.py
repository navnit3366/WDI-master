print('Podaj system, z ktorego chcesz przeliczyc: ', end=' ')
system1 = int(input())
print('Wczytaj liczbe w wybranym systemie: ', end=' ')
number = input()
print('Podaj system, na ktory chcesz przeliczyc: ', end=' ')
system2 = int(input())
print('Podana liczba w systemie {}-kowym to '.format(system2), end='')

#ZAMIANA NA 10
length = len(number)
new = 0

for i in number:
    a = int(i)*(system1**(length-1))
    new = new + a
    length-=1

#ZAMIANA NA DOWOLNY
lenght2 = len(str(new))
tab = []

while new>0:
    mod = new%system2
    tab.append(mod)
    new = int((new-mod)/system2)
tab.reverse()
for i in tab:
    print(i, end='')