from random import randint

import time
start_time = time.time()

tab = []
size=50
while (size>0):
    tab.append(randint(1,100))
    size-=1
print(tab)

def quick(tab,left,right):
    pivot = left
    l=left
    r=right

    while (r>l):
        if (pivot == l):
            if (tab[r] < tab[pivot]):
                tab[r],tab[pivot]= tab[pivot], tab[r]
                pivot = r
                l+=1
            else:
                r-=1

        if (pivot == r):
            if (tab[l] > tab[pivot]):
                tab[l], tab[pivot] = tab[pivot], tab[l]
                pivot = l
                r-=1
            else:
                l+=1

    if (r+1<right):
        quick(tab,r+1,right)
    if (l>left):
        quick(tab,left,l-1)
    return(tab)
quick(tab,0,len(tab)-1)

print("--- %s seconds ---" % (time.time() - start_time))

print(quick(tab,0,len(tab)-1))