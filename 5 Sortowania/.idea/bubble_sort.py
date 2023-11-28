from random import randint

import time
start_time = time.time()

tab = []
size=50
while (size>0):
    tab.append(randint(1,100))
    size-=1
print(tab)

def bubble(b):
    tab_bubble=b
    length=len(tab_bubble)-1
    sorted=False
    while not sorted:
        sorted=True
        for i in range(length):
            if tab_bubble[i]>tab_bubble[i+1]:
                sorted=False
                tmp=tab_bubble[i]
                tab_bubble[i]=tab_bubble[i+1]
                tab_bubble[i+1]=tmp
    return(tab_bubble)
bubble(tab)

print("--- %s seconds ---" % (time.time() - start_time))

print(bubble(tab))