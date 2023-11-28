def fibo_rek(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo_rek(n-2)+fibo_rek(n-1)
print("Wpisz ktory wyraz ciagu fibonacciego chcesz obliczyc:", end=' ')
x = int(input())
print("{}-ty wyraz ciagu wynosi:".format(x), end=' ')
print(fibo_rek(x-1))

def fibo_iter(m):
    if m==0:
        return 0
    elif m==1:
        return 1
    else:
        a=0
        for j in range (1,m+1):
            a=a+j
        return a
print("Wpisz ktory wyraz ciagu fibonacciego chcesz obliczyc:", end=' ')
y = int(input())
print("{}-ty wyraz ciagu wynosi:".format(y), end=' ')
print(fibo_rek(y-1))
