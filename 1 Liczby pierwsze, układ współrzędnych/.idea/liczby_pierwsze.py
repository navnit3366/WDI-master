import time

start_time = time.time()

tab = []

for a in range(2,1000):
    b=2
    while a<1000:
        if a%b==0 and b<a:
            break
        elif b==a:
            tab.append(a)
            break
        else:
            b+=1

for x in tab:
    print(x)

print("--- %s seconds ---" % (time.time() - start_time))