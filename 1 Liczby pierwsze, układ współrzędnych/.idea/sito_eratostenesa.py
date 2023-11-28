from math import ceil, sqrt

n = int(input('Wpisz n: '))

tab = []

for i in range(2,n):
    tab.append(i)

a = ceil(sqrt(n))

for j in range(2,a+1):
    if j in tab:
        for i in range(2,n):
            if i in tab:
                if i%j==0 and i!=j:
                    tab.remove(i)
            else:
                continue
    else:
        continue
print(tab)