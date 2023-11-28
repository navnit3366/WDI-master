from math import sqrt

print("Podaj dlugosc boku a: ", end=' ')
a=int(input())
print("Podaj dlugosc boku b: ", end=' ')
b=int(input())
print("Podaj dlugosc boku c: ", end=' ')
c=int(input())

p=(a+b+c)/2
Pole=sqrt(p*(p-a)*(p-b)*(p-c))

print("Pole trojkata wynosi: ", end=' ')
print(Pole)