alfabet='abcdefghijklmnopqrstuvwxyz'
tekst='Walcz o pilke jak lwica'
klucz='karola'

def z_kluczem(alfabet,tekst,klucz):
    tekst=tekst.lower()
    tekst=tekst.replace(' ','')

    nowy=''
    j=0
    for i in range(0,len(tekst)):
        index_znaku_z_klucza_w_alfabecie=alfabet.find(klucz[j])
        index_znaku_z_klucza_w_alfabecie+=1
        print(index_znaku_z_klucza_w_alfabecie)
        kolejny_znak_tekstu=tekst[i]
        index_kolejnego_znaku_tekstu_w_alfabecie=alfabet.find(kolejny_znak_tekstu)
        index_nowej_litery=index_znaku_z_klucza_w_alfabecie+index_kolejnego_znaku_tekstu_w_alfabecie
        if (index_nowej_litery>25):
            index_nowej_litery=index_nowej_litery-26
        zaszyfrowana_litera=alfabet[index_nowej_litery]
        nowy=nowy+zaszyfrowana_litera
        j+=1
        if(j%6==0):
            j=0
    print(nowy)
z_kluczem(alfabet,tekst,klucz)
