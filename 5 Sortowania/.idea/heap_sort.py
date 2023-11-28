from random import randint

import time
start_time = time.time()

tab = []
size=50
while (size>0):
    tab.append(randint(1,100))
    size-=1
print(tab)

def heap_swap(tab,parent,l):
    child=parent*2
    if child<=l:
        if l>child:
            if tab[child-1]<tab[child]:
                child=child+1
        if tab[parent-1]<tab[child-1]:
            tab[parent-1],tab[child-1]=tab[child-1],tab[parent-1]
            heap_swap(tab,child,l)

def heap(tab):
    for i in range (int((len(tab))/2),0,-1):
        heap_swap(tab,i,len(tab))
    for i in range (len(tab)-1,0,-1):
        tab[i],tab[0]=tab[0],tab[i]
        heap_swap(tab,1,i)
    return tab
heap(tab)

print("--- %s seconds ---" % (time.time() - start_time))

print(heap(tab))