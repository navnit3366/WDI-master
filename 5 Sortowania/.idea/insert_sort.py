from random import randint

import time
start_time = time.time()

tab = []
size=50
while (size>0):
    tab.append(randint(1,100))
    size-=1
print(tab)

def insert(i):
    tab_insert=i
    length=len(tab_insert)
    for k in range(1,length):
        sortowany=tab_insert[k]
        while (sortowany<tab_insert[k-1] and k>0):
            tab_insert[k]=tab_insert[k-1]
            k-=1
        tab_insert[k]=sortowany
    return(tab_insert)
insert(tab)

print("--- %s seconds ---" % (time.time() - start_time))

print(insert(tab))