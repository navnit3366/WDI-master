dlugosci_miesiecy = [31,28,31,30,31,30,31,31,30,31,30,31]

rok = 2001
miesiac = 0
dzien_miesiaca = 0
dzien_tygodnia = 0
ilosc_dni_miesiaca = 0
licznik = 0

while rok <= 2014:
    while miesiac < 12:
        ilosc_dni_miesiaca = dlugosci_miesiecy[miesiac]
        while dzien_miesiaca < ilosc_dni_miesiaca:
            dzien_miesiaca += 1
            dzien_tygodnia += 1
            if dzien_miesiaca == 13 and dzien_tygodnia == 5:
                licznik += 1
            elif dzien_tygodnia == 7:
                dzien_tygodnia = 0
        miesiac += 1
        dzien_miesiaca = 0
    miesiac = 0
    rok += 1
    if rok%4 == 0:
        dlugosci_miesiecy[1] = 29
    else:
        dlugosci_miesiecy[1] = 28
print('Piatkow 13-tego w latach 2001-2014 jest',licznik)