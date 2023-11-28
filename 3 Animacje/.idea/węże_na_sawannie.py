import random

size = int(input('Podaj rozmiar sawanny: '))

#poczatkowa tablica weza
snake = []

a = random.randint(0,size-1)
snake.insert(0, a)
snake.insert(0, a)
snake.insert(0, a)

while(len(snake)<size):
    a = random.randint(0,size-1)
    while a==snake[0]:
        a = random.randint(0, size-1)
    snake.insert(0, a)
    snake.insert(0, a)
    snake.insert(0, a)

for k in range(2):
    a = random.randint(0, size-1)
    while a==snake[0]:
        a = random.randint(0, size-1)
    for i in range(3):
        snake.insert(0, a)
        for i in range(size):
            for j in range(size):
                if snake[i] == j:
                    print('o', end=' ')
                else:
                    print('.', end=' ')
            print()
        print()
        snake.pop(size-1)