size = int(input('Podaj nieparzysty wymiar planszy: '))
a = int((size+1)/2)

#od duzego do malego
for k in range(a):
    for i in range(size):
        for j in range(size):
            if (i==j or size-1-i==j) and i>=k and i<size-k:
                print('x',end=' ')
            else:
                print('.',end=' ')
        print()
    print()

#od malego do duzego
for k in range(a-1,-1,-1):
    for i in range(size):
        for j in range(size):
            if (i==j or size-1-i==j) and i>=k and i<size-k:
                print('x',end=' ')
            else:
                print('.',end=' ')
        print()
    print()