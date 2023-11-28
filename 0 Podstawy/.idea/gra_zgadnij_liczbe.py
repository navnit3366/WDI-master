import random
losowana = random.randrange(10)

print("Twoim zadaniem jest zgadniecie wylosowanej liczby od 0 do 10, jaka wybierasz?: ", end=' ')
liczba=int(input())

while(liczba!=losowana):
    if(liczba<losowana):
        print("Zbyt mala, podaj wieksza liczbe!")
    elif(liczba>losowana):
        print("Zbyt duza, podaj mniejsza liczbe!")
    liczba = int(input())

print("Gratulacje!")