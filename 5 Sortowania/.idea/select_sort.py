from random import randint

import time
start_time = time.time()

tab = []
size=50
while (size>0):
    tab.append(randint(1,100))
    size-=1
print(tab)

def select(s):
    tab_select=s
    length=len(tab_select)

    for j in range(length-1):
        najmniejszy=j
        for i in range(j+1,length):
            if tab_select[i]<=tab_select[najmniejszy]:
                najmniejszy=i
        tmp=tab_select[j]
        tab_select[j]=tab_select[najmniejszy]
        tab_select[najmniejszy]=tmp
    return(tab_select)
select(tab)

print("--- %s seconds ---" % (time.time() - start_time))

print(select(tab))