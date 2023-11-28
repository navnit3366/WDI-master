print('Trasa to kod w postaci ciagu na przemian liter i cyfr np A5F3C2')
a = input('Wpisz trase 1. tramwaju: ')
b = input('Wpisz trase 2. tramwaju: ')
#a = 'A5F3C2'
#b = 'B4F4G1'

time1 = 0
for i in range(len(a)):
    if i%2!=0:
        time1 += int(a[i])
    else:
        continue
print('Czas przejazdu 1. tramwaju to: ', time1)

time2 = 0
for i in range(len(b)):
    if i%2!=0:
        time2 += int(b[i])
    else:
        continue
print('Czas przejazdu 2. tramwaju to: ', time2)

tab_a = []
for i in range(len(a)):
    if i%2!=0:
        for j in range(int(a[i])):
            tab_a.append(a[i-1])
#print(tab_a)

tab_b = []
for i in range(len(b)):
    if i%2!=0:
        for j in range(int(b[i])):
            tab_b.append(b[i-1])
#print(tab_b)

if len(tab_a)>len(tab_b):
    table = tab_b
else:
    table = tab_a

tab_a_b = []
for i in range(len(table)):
    if tab_a[i] == tab_b[i]:
        tab_a_b.append(i+1)

if len(tab_a_b)!=0:
    print('Tramwaje spotkaja sie w ', end='')
    for i in tab_a_b:
        print(i,',',end='')
    print('jednostkach czasu')
else:
    print('Tramwaje sie nie spotkaja :(')