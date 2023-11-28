tekst='Przyszlosc Polskiej Informatyki'

print('Wpisz o ile znakow chcesz przesunac: ')
ile=int(input())

def cezar(tekst,ile):
    tekst=tekst.lower()
    tekst=tekst.replace(' ','')

    nowy=''
    for i in range (len(tekst)):
        x=ord(tekst[i])
        x=x+ile
        if (x>122):
            x=x-26
        a=chr(x)
        nowy=nowy+a
    print(nowy)
cezar(tekst,ile)