from random import randint

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
print(bubble(tab))

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
print(select(tab))

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
print(insert(tab))

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

print(quick(tab,0,len(tab)-1))

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
print(heap(tab))