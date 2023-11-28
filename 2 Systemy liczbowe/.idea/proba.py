liczba=input()
for i in liczba:
    alf = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
    if i in alf:
        g=alf.index(i)+10
    print(g)