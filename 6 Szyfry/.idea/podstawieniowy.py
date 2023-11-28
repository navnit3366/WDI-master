alfabet='abcdefghijklmnopqrstuvwxyz'
nalfabet=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

tekst='Agnieszka Miszkurka'

def podstawieniowy(tekst,alfabet,nalfabet):
    tekst = tekst.lower()
    tekst = tekst.replace(' ', '')

    nowy = ''
    for i in range (len(tekst)):
        x=alfabet.find(tekst[i])
        if (x>25):
            x=x-25
        a=nalfabet[x]
        nowy=nowy+a
    print(nowy)
podstawieniowy(tekst,alfabet,nalfabet)