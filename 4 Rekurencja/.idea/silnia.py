def silnia_rek(n):
    if (n==0 or n==1):
        return 1
    else:
        return silnia_rek(n-1)*n
print("Wpisz liczbe n do obliczenia n! :", end=' ')
x=int(input())
print("Silnia od {} wynosi:".format(x), end=' ')
print(silnia_rek(x))

def silnia_iter(m):
    if (m==0 or m==1):
        return 1
    else:
        a=1
        for i in range(2, x + 1):
            a=a*i
        return a
print("Wpisz liczbe m do obliczenia m! :", end=' ')
y = int(input())
print("Silnia od {} wynosi:".format(y), end=' ')
print(silnia_iter(y))